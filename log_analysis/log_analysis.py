import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from log_parse import log_parse
from collections import Counter
from log_pdf import PDF


with open("apache_logs") as file:
    logs = file.readlines()

first_line = logs[0]
first_line = first_line.split()
"""What is the status code of the first line?"""
print(f'The first line HTTP Status Code is {first_line[8]}.\n')
"""2xx successful – the request was successfully received, understood, and accepted"""

log_data = [log_parse(line) for line in logs]
count_df = pd.DataFrame.from_dict(log_data)

status_code_i = [(i, log_data[i]['status_code']) for i, line in enumerate(log_data)]
status_code = [(log_data[i]['status_code']) for i, line in enumerate(log_data)]

status_200 = [(status_code_i[i]) for i, tup in enumerate(status_code_i) if status_code_i[i][1] == 200]
status_404 = [(status_code_i[i]) for i, tup in enumerate(status_code_i) if status_code_i[i][1] == 404]

print(f'Number of HTTP Status Code 404 is: {len(status_404)}.')


num_error_code = set(status_code) - {200}
print(f'The total number of different error codes found is: {len(set(status_code) - {200})}.')

counter = Counter(status_code)
c_dict = dict(counter)

top_keys = [key for i, key in enumerate(c_dict.keys()) if i < 3]
print(f'The top three status codes are: {top_keys}.\n')

lines_with_404 = list(filter(lambda x: x['status_code'] == 404, log_data))

resource_list = [line['request_type'] for line in lines_with_404]
print(f"I found {len(set(resource_list))} different error producing URL's in this log file.")
c = Counter(resource_list)

top_problem_url = [key for key, _ in c.most_common(3)]
print(f"The top 3 problem URL's are: {Counter(resource_list).most_common(3)}.\n")  


status_code_str = [str(x) for x in status_code]

sns.set_theme()
sns_status_code = sns.histplot(status_code_str, color = 'blue')
sns_status_code.set(title="Status Codes")
sns_status_code.figure.savefig("status_codes.png", bbox_inches = 'tight')
sns_status_code.figure.clf()

re_404 = pd.DataFrame(resource_list)

plt.figure(figsize=(10, 8))
sns_status_code = sns.histplot(re_404, color = 'blue', x=0)
sns_status_code.set(title="404 Error Producing Requests")
plt.xticks(fontsize=8)
plt.xticks(rotation = 90)
sns_status_code.figure.savefig("resource_list.png", bbox_inches = 'tight')
sns_status_code.figure.clf()


list_plots =["status_codes.png", "resource_list.png"]

log_report = PDF()

for plot in list_plots:
    log_report.print_page(plot)
log_report.output("LogReport.pdf", "F")

print('Done')