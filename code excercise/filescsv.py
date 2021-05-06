# from _csv import writer
# from csv import writer
# with open("file1.csv",'w') as f:
#     f1_writer=writer(f)
#     for i in range(100):
#              f1_writer.writerow([i+1 ,":" ,'sanket'])
from  csv import DictWriter
with open("final.csv","w",newline="") as f:
    s1=DictWriter(f,fieldnames=["name","age","er_no"])
    s1.writeheader()
    s1.writerows(
        [
            {'name':'sanket','age':19,"er_no":180010107027},
            {'name':'rajesh','age':19,"er_no":180010107023},
            {'name':'sanket','age':19,"er_no":180010107029},
            {'name':'rajesh','age':19,"er_no":180010107026},
            {'name':'sanket','age':19,"er_no":180010107028},
            {'name':'rajesh','age':19,"er_no":180010107023},
            {'name':'sanket','age':19,"er_no":180010107022},
            {'name':'rajesh','age':19,"er_no":180010107024},



        ]
    )