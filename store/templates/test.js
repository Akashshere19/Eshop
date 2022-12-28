// var name = "Akash"
// var fname  = "akash shere"
// var isStudent = false
// var skill = ["python","django","js","tornado","html"]
// var age = 26
// console.log(name,fname,skill,isStudent)
// console.log(typeof(name),typeof(fname),typeof(isStudent),typeof(skill))
// console.log('my name is '+ name +' and Age is: '+ age)

const http = require("http")
console.log(http)
http
   .createServer((req,res)=>{
    console.log('Request Reci..');
    res.write("<h1>hi   .....</h1>");
    res.end();

   })
   .listen(3000);