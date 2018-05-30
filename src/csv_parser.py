from glob import glob

ID_COL = "id"
DATE_COL = "ydt"
DESC_COL = "description"
DEBT_COL = "debit"
CRDT_COL = "credit"
BLNC_COL = "balance"


def get_csv(path, out, i):
    with open(path) as f:
        for line in f:
            line = line.replace(',,', ',0,')
            out.write(str(i) + "," + line)
            i += 1
    return i


def combine_csvs():
    paths = glob("../statements/*.csv")
    i = 1
    with open("../combined_statements.csv", "w+") as output_file:
        output_file.write(ID_COL+","+DATE_COL+","+DESC_COL+","+DEBT_COL+","+CRDT_COL+","+BLNC_COL)
        for path in paths:
            i = get_csv(path, output_file, i)


if __name__ == "__main__":
    combine_csvs()
