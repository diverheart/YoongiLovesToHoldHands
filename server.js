
const express = require("express");
const app=express();
const path = require('path');
const bodyParser = require('body-parser');
var handle;
const {PythonShell} =require('python-shell');
 


app.use(bodyParser.urlencoded({ extended: true })); 
app.use(express.static("public"));



//Router to handle the incoming request.
app.get('/run', (req, res, next)=>{
    //Here are the option object in which arguments can be passed for the python_test.js.
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
           //If you are having python_test.py script in same folder, then it's optional.
        args:[String(handle)] //An argument which can be accessed in the script using sys.argv[1]
    };


      
  
    PythonShell.run('app.py', options, function (err, result){
          // if (err) throw err;
          // result is an array consisting of messages collected 
          //during execution of script.
          try
          {
          console.log('result: ', result.toString());
          res.sendFile(path.join(__dirname+'/index.html'));

          if(result.toString()=="404")
          {
            res.redirect("/error");
          }
          
        }

        catch(err)
        {console.log(err);
          res.redirect("/error");
          
        
         
      }

      // finally
      // {
      //    res.redirect("/");
      // }
    });

});



app.post('/running', function(req,res)
{
	handle=req.body.hname;
	res.redirect('/run');
	



})


app.get('/', function(req,res)
{
	 res.sendFile(path.join(__dirname+'/index.html'));
})

app.get('/error',function(req,res)
{
     res.sendFile(path.join(__dirname+'/error.html'));
});
app.listen(3000, function()
	{
		console.log("Server connected to port 3000");
	});
