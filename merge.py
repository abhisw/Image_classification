
read_files = ['Motorcycle.txt','neg_neg_yadavcar.txt','neg_neg_yadavcarvs5.txt','neg_neg_car.txt','neg_neg_car_auto.txt','neg_temp.txt']
#read_files = ['pos_two/p3.txt','pos_two/p4.txt','pos_two/p5.txt','pos_two/p1.txt','pos_two/p2.txt']

#read_files = ['pos_car.txt','car.txt'] #two_whl_tmp.info','pos_two.txt']

open('bg_car_alone.txt', 'w').close()

with open("bg_car_alone.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
