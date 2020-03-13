import subprocess
from statistics import stdev, mean

#geometry_filepath = "nx96_ny96_nl24_ne8_ntheta26"
geometry_filepath = "nx192_ny64_nl27_ne12_ntheta32"

summary_filename = "/".join([geometry_filepath, "profiling_summary.csv"])
all_trials_filename = "/".join([geometry_filepath, "profiling_all_trials.csv"])

# Parse jobs description array
import json
jobs_filename = "/".join([geometry_filepath, "jobs.json"])
with open(jobs_filename, 'r') as f:
    jobs = json.load(f)

with open(all_trials_filename, 'w') as all_trials_file:
    with open(summary_filename, 'w') as summary_file:
        # Write headers for output files
        all_trials_file.write("version, nprocs, field_time, advance_time\n")
        summary_file.write("version, nprocs, mean_field_time, stdev_field_time, mean_advance_time, stdev_advance_time\n")

        for job in jobs:
            field_times = []
            advance_times = []
            for trial_filename in job['trial_files']:
                # Get bash command that will process one job file
                trial_filepath = str(job['nprocs']) + "_" + str(job['version'])
                arg = "/".join([geometry_filepath, trial_filepath, trial_filename])
                print(arg)
                command = "./process_job_output.sh "+ arg

                # Run the bash script to process the job file
                # If the file is taking more than 2 sec to parse something is likely wrong
                result = subprocess.run(command.split(), stdout=subprocess.PIPE, \
                    stderr=subprocess.PIPE, timeout=2)
                line = result.stdout.decode('utf-8')

                # Collect statistics in the job file
                [field_time, advance_time] = line.split(",")
                print(field_time, advance_time)
                field_times.append(float(field_time))
                advance_times.append(float(advance_time))
                all_trials_file.write(job['version'] + ", " + str(job['nprocs']) + ", " + line)
               
            # Write summary statistics
            summary_file.write(job['version'] + ", " + str(job['nprocs']) + ", " + \
            str(mean(field_times)) + ", " + str(stdev(field_times)) + ", " + \
            str(mean(advance_times)) + ", " + str(stdev(advance_times)) + "\n")

