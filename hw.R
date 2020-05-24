# 利用Vector找出異常的BMI
height = c(180, 169, 173)
weight = c(73, 87, 43)
stu = c('Brian', 'Toby', 'Sherry')
BMI = weight/(height/100)^2
names(BMI) = stu
BMI[BMI<18.5|BMI>=24]
