s = open("swati.html","w")
a = """<html>
 <head>
<title>RESUME</title>

<style type="text/css">
    table {
        font-size: 20px;
    }
    #heading{
        font-size: 20px;
        }
</style>
</head>
<body>
<div >
  <center><h1><u>MY RESUME</u></h1></center>  
<h3> Swati Meshram</h3>
<p> Swatimesgram200@gmail.com</p>
<p>DOB: 18-12-2000</p>
<p>Narayan Nagar Bhopal</p
<p>Contact No.:   83490 64981</p>
 
  <h2><u>CAREER OBJECTIVE</u></h2>
  <p>To succeed in an environment of growth 
     and excellence in computer science and 
     earn a job which provide me job satisfaction
     and self development and help me in achieving
      personal as well as organization goals.</p>
            <h2><u>EDUCATION </u></h2>
            <table border="1">
                <tr >
                    <th>Qualification</th>
                    <th>Institute</th>
                    <th>Percentage / Grades</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>10th</td>
                    <td>Govt. High School Ukwa</td>
                    <td> 77%</td>
                    <td>2016</td>
                </tr>
                <tr>
                    <td>12th</td>
                    <td>Govt. Higher Secondary  School Ukwa</td>
                    <td>67%</td>
                    <td>2018</td>
                </tr>
                <tr>
                    <td>1st Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>6.5 SGPA</td>
                    <td>2019</td>
                </tr>
                <tr>
                    <td>2nd Sem</td>
                    <td>Barkatullah University Institute<br> Of Technology Bhopal</td>
                    <td>5.6 SGPA</td>
                    <td>2019</td>
                </tr>
                
            </table>
        </div>
         <h2><u>HOBBIES</u></h2>
          <p> Study </p>
           <p>Dance</p>
           <p></p>

          <h2><u>LANGUAGES</u></h2>
           <p>Hindi</p>
           <p>English.</p> 
          <h2><u>SKILLS</u></h2>
           <p>C</p><p>C++</p>
         <h2><u>WORK  EXPERIENCE</u></h2>
        <p>Fresher.</p>

</body>
</html>"""
s.write(a)
s.close()