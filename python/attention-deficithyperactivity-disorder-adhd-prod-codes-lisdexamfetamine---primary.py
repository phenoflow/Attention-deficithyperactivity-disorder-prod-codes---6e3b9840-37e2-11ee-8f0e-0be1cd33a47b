# Adrian J Hire, Darren M Ashcroft, David A Springate, Douglas T Steinke, 2023.

import sys, csv, re

codes = [{"code":"13238","system":"readv2"},{"code":"16185","system":"readv2"},{"code":"47609","system":"readv2"},{"code":"47679","system":"readv2"},{"code":"51453","system":"readv2"},{"code":"55169","system":"readv2"},{"code":"55987","system":"readv2"},{"code":"57786","system":"readv2"},{"code":"9738","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('attention-deficithyperactivity-disorder-prod-codes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["attention-deficithyperactivity-disorder-adhd-prod-codes-lisdexamfetamine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["attention-deficithyperactivity-disorder-adhd-prod-codes-lisdexamfetamine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["attention-deficithyperactivity-disorder-adhd-prod-codes-lisdexamfetamine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
