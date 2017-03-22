from ofxparse import OfxParser

with open('./extrato.ofx') as file:
    ofx = OfxParser.parse(file)
    print ofx.accounts
    for account in ofx.accounts:
        print account.number
        print account.statement.start_date
        print account.statement.end_date
