htmlHeader = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Olin Web Literacy (and Design)</title>
        
        <link rel="stylesheet" href="../stylesheets/style.css"/>

    </head>
    <body>        
        <nav>
            <ul>
                <li class="title"><a href="../index.html">OWL</a></li>
                <li><a href="../index.html">Home</a></li>
                <li><a href="../students.html">Announcements</a></li>
                <li><a href="../resources.html">Resources</a></li>
                <li><a href="../schedule.html">Schedule</a></li>
                <li><a href="../docs/OWLit Syllabus.pdf">Syllabus</a></li>
                <li class="rightover"><a href="mailto:olinweblit@lists.olin.edu">QUESTIONS</a></li>
            </ul>
        </nav>
        
        <menu>
            <!-- FOR CLASS SUMMARY LINKS -->
            <ul>
                <li><a href="class-02.html">Class 2: Jan 24</a></li>
                <li><a href="class-01.html">Class 1: Jan 21</a></li>
            </ul>
        </menu>
        
    <section id="splash">
        <div class="wrapper">
'''

htmlFooter = '''  
        </div class="wrapper">
    </section>
    
    <footer>
            &copy; 2014 Olin Web Literacy and Design | <a href="http://olin.edu">Olin College of Engineering</a>
        </footer>
        
    </body>
</html>
'''


# CLASSES
class01 = '''
        <h3>Class 1: Jan 21</h3>
        
        <h4>Goal:</h4> 
        <p>Give basic over-view of what will be going on in the class and what tools we will be working with.</p>
        
        <h4>Due:</h4>
        <p>N/A</p>
        
        <h4>Homework:</h4>
        <p>IS Form</p>
        
        <h4>Summary:</h4>
        <ol>
            <li>Went over syllabus</li>
            <li>Opened up a few example portfolio websites from syllabus:
               <ul>
                    <li>What are some of the first things you notice about the site in terms of design?</li>
                    <li>Portfolios reflect the person who made them</li>
                    <li>Ctrl+U shortcut to show the front end (intro to HTML)</li>
                </ul></li>
            <li>Setup/Opened up text-editor (Sublime) to write first Hello World webpage
                <ul>
                    <li>Basic structure of an HTML page</li>
                    <li>Briefly covered tags: div, h1, p</li>
                </ul></li>
            <li>Created basic CSS file (set the text in a div to blue)
                <ul>
                    <li>Briefly touched on hex-codes, will get into more detail later</li>
                    <li>Showed how to include external CSS file</li>
                    <li>How to include style straight on the page without file (and that not recommended)</li>
                    <li>How to add inline-styling (and that not recommended)</li>
                    <li>Show how CSS has hierarchy and priority</li>
                </ul></li>
            <li>Created basic JS file (alert)
                <ul>
                    <li>Showed how to include external JS file</li>
                    <li>Location in head vs. location in body</li>
                </ul></li>
        </ol>
        
        <h4>Download In-Class Example:</h4>
        <p><a href="classExample/class1-eg/class1-eg.zip">class1-eg.zip</a></p>
        
        <h4>Screencast RECAP session:</h4>
        <p>(Currently Unavailable)</p>
'''

class02 = '''
        <h3>Class 2: Jan 24</h3>
        
        <h4>Due:</h4>
        <p>IS Form</p>
        
'''


def generate():
    allClasses = [class01, class02]
    classCount = len(allClasses)
    for classNum in range(classCount):
        #Make the filename
        toName = "class-"
        if classNum < 10:
            toName = toName + "0" + str(classNum + 1)
        else:
            toName = toName + str(classNum) 
        filename = '%s.html' %toName
        f = open(filename, 'w')
        f.write(htmlHeader)
        f.write(allClasses[classNum])
        f.write(htmlFooter)
        
        f.close()


generate()