f = open("C:/Users/student.MCALAB/Desktop/20MCA007/PYTHON 1/car.csv", 'a')
import json
thisdict = {
"brand":"ford",
"model":"mustang",
"year":"1964"
}
result =json.dumps(thisdict)
f.write(result)
f.close()
f = open("C:/Users/student.MCALAB/Desktop/20MCA007/PYTHON 1/car.csv", 'r')
print(f.read())