import os 


def main():
  i =0
  path="/Users/najah/Desktop/devmiddle/programming/python_six_projects/images/"
  for filename in os.listdir(path):
    my_dest='images'+'_'+str(i)+".jpg"
    my_source=path+filename
    my_dest=path+my_dest
    os.rename(my_source,my_dest)
    i+=1



if __name__=='__main__':
  main()