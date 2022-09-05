class Job:
    def __init__(self, cluster, job_id, name, status, submit_time, start_time, run_time, time_left, nodes, cpus, memory, comment=""):
        self.cluster     = cluster
        self.job_id       = job_id
        self.name        = name
        self.status      = status
        self.submit_time  = submit_time
        self.start_time   = start_time
        self.run_time     = run_time
        self.time_left    = time_left
        self.nodes       = nodes
        self.cpus        = cpus
        self.memory      = memory
        self.is_finished  = False
        self.cpu_time     = ""
        self.end_time     = ""
        self.comment     = comment
    def update(self, status, run_time, time_left, is_finished=False, cpu_time=0, end_time=""):
        self.run_time     = run_time
        self.time_left    = time_left
        self.status      = status
        self.is_finished = is_finished
        self.cpu_time    = cpu_time
        self.end_time    = end_time
    def __eq__(self, job_id, cluster=None):
        '''
            Overload of the == operator for the Job class. Compares only the job_id with an int

            Parameters:
            -----------
                int     : job_id
                    job_id to compare
            Return:
            -------
                bool
                    True if this is the same jobid, false else
        '''
        if cluster is not None:
            return self.job_id == job_id and self.cluster == cluster
        else:
            return self.job_id == job_id
    def __str__(self):
        l = "Job ID : {:.0f} :\n".format(self.job_id)
        l += "\tName                 : {:s}\n".format(self.name)
        l += "\tStatus               : {:s}\n".format(self.status)
        l += "\tSubmitted            : {:s}\n".format(self.submit_time)
        if self.status == "PENDING":
            l += "\tEstimated start time : {:s}\n".format(self.start_time)
        else:
            l += "\tStart time           : {:s}\n".format(self.start_time)
            if self.status == "RUNNING":
                l += "\tTime left            : {:s}\n".format(self.time_left)
                l += "\tRunning time         : {:s}\n".format(self.run_time)
                l += "\tNumber of nodes      : {:.0f}\n".format(self.nodes)
                l += "\tNumber of CPUs       : {:.0f}\n".format(self.cpus)
                l += "\tMemory allocated     : {:s}\n".format(self.memory)
            else:
                l += "End time           : {:s}\n".format(self.end_time)
                l += "Wall time          : {:s}\n".format(self.run_time)
                l += "Total CPU time     : {:s}\n".format(self.cpu_time)
        return l
