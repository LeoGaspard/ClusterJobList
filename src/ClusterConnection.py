import paramiko
from plyer import notification

from Job import Job

class ClusterConnection:
    def __init__(self, name, host, user, key_file, gateway=None):
        '''
            Constructor of the ClusterConnection class. Currently only works when the 
            cluster queue is SLURM

            Parameters:
            -----------
                name        : str
                    The name given to this host
                host        : str
                    Name of the host
                user        : str
                    Username on host
                key_file    : str
                    Path to the ssh key file that connects to host (and gateway)
                gateway     : tuple of str
                    Username and host for the gateway sonnection. e.g. ("toto", "cluster_client.fr")
        '''

        self.name     = name
        self.host     = host
        self.user     = user
        self.key_file = key_file
        self.gateway  = gateway

        #TODO read jobs stored in a file 
        self.job_list  = []
    def __str__(self):
        return self.name

    def print_jobs(self):
        '''
            Prints the jobs stored in job_list
        '''
        print("="*70)
        print("="+"{:^68s}".format(self.name)+"=")
        print("="*70)
        for job in self.job_list:
            print(job)
        print()

    def update_jobs(self, notification_mode):
        '''
            Recover the list of running jobs
        '''

        self.SSH = self.__connect(self.host, self.user, self.key_file, gateway=self.gateway)

        command = 'squeue --format="%.18i %.6C %.6D  %.10L  %.8m  %.6M  %.25S %.15T %.25V %.30j" -h -u {:s}'.format(self.user)
        stdin, stdout, stderr = self.SSH.exec_command(command)
        lines = stdout.readlines()

        jobidlist = []

        for job in lines:
            job         = job.split()
            job_id       = int(job[0])
            cpus        = int(job[1])
            nodes       = int(job[2])
            time_left    = job[3]
            memory      = job[4]
            run_time     = job[5]
            start_time   = job[6].replace("T", " ")
            status      = job[7]
            submit_time  = job[8].replace("T", " ")
            name        = job[9]

            jobidlist.append(job_id)

            if job_id in self.job_list:
                ind = self.job_list.index(job_id)
                if self.job_list[ind].status in ['PENDING', 'CONFIGURING'] and status == 'RUNNING' and notification_mode in ['Job start + job end', "Job start"]:
                    notification.notify(
                               title = "Job {:.0f} started".format(job_id),
                               message="{:s}".format(name) ,
                               # displaying time
                               timeout=10
                   )
                elif self.job_list[ind].status == 'RUNNING' and status != 'RUNNING' and notification_mode in ['Job start + job end', "Job end"]:
                    notification.notify(
                               title = "Job {:.0f} ended".format(job_id),
                               message="{:s}".format(status) ,
                               # displaying time
                               timeout=10
                   )
                self.job_list[ind].update(status, run_time, time_left)
            else:
                self.job_list.append( Job(self.name, job_id, name, status, submit_time, start_time, run_time, time_left, nodes, cpus, memory) )

        for job in self.job_list:
            if job.job_id not in jobidlist:
                # This means a job has finished
                command = 'sacct --jobs {:.0f} --format=end,CPUTime,Elapsed,State%50 -n'.format(job.job_id)
                stdin, stdout, stderr = self.SSH.exec_command(command)
                line = stdout.readlines()[0].split()

                endTime = line[0].replace("T", " ")
                cpuTime = line[1]
                run_time = line[2]
                status  = line[3]
                if "CANCELLED" in status:
                    status = "CANCELLED"
                if notification_mode in ['Job start + job end', "Job end"]:
                    notification.notify(
                               title = "Job {:.0f} ended".format(job.job_id),
                               message="{:s}".format(status) ,
                               # displaying time
                               timeout=10
                   )
                job.update(status, run_time, "", is_finished=True, cpu_time=cpuTime, end_time=endTime)
        self.SSH.close()

    def __connect(self, host, user, key_file, gateway=None):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sock = None
        if gateway:
            gw_client = self.__connect(gateway[1], gateway[0], key_file)
            sock = gw_client.get_transport().open_channel(
                'direct-tcpip', (host, 22), ('', 0)
            )
        kwargs = dict(
            hostname=host,
            port=22,
            username=user,
            key_filename=key_file,
            sock=sock,
            banner_timeout=20,
        )
        client.connect(**kwargs)
        return client
