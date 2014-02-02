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
                <li><a href="class-04.html">Class 5: Feb 4</a></li>
                <li><a href="class-04.html">Class 4: Jan 31</a></li>
                <li><a href="class-03.html">Class 3: Jan 28</a></li>
                <li><a href="class-02.html">Class 2: Jan 24</a></li>
                <li><a href="class-01.html">Class 1: Jan 21</a></li>
            </ul>
        </menu>
        
    <section id="splash">
        <div class="wrapper">
'''

htmlFooter = '''  
        </div>
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
        
        <h4>Goal:</h4>
        <p>Discuss clients vs. servers and what exactly happens when you type a url into a browser. 
        <p>Show off web inspector -- mess with sites.</p>
        <p>Introdocue lists, web navigation, and structure.</p>
        
        <h4>Due:</h4>
        <p>IS Form</p>
        
        <h4>Homework:</h4>
        <p>Modify the nav/menu and think about how to organize portfolio website (with JS and animation, minimalism, multiple pages, etc.)</p>
        
        <h4>Summary</h4>
        <ol>
            <li>Lecture
                <ul>
                    <li>Internet vs. Web</li>
                    <li>Front End/Client Side vs. Back End/Server Side</li>
                    <li>What is the DOM? Basic DOM structure</li>
                    <li>Browsers, how they work, what is different about them?</li>
                    <li>What happens when you enter a URL?</li>
                </ul></li>
            <li>Showed off web inspector in Google Chrome
                <ul>
                    <li>How to see the front-end structure of a site</li>
                    <li>How to manipulate CSS styles with inspector</li>
                    <li>Console gives errors of page, can run script from it, will be useful later</li>
                </ul></li>
            <li>In class work:
                <ul>
                    <li>List elements, &lt;ol&gt; vs. &lt;ul&gt;
                    <li>The different types of links
                        <ul>
                            <li>To external sites (in current tab vs. new tab)</li>
                            <li>File in same folder, in subfolder, in parent folder</li>
                            <li>On page anchors</li>
                            <li>Mailto</li>
                            <li>Link place holder (#)</li>
                        </ul></li>
                </ul></li>
            <li>Showed different types of styling in terms of page/site structure and navigation
                <ul>
                    <li>Appending all section on one page and jumping to with anchors</li>
                    <li>Hiding all sections but the active, click link to switch what is active</li>
                    <li>Having multiple .html pages and using regular links to get to them</li>
                </ul></li>
        </ol>
        
        <h4>Further Reading:</h4>
        <p><a href="http://www.whatismyip.com/what-is-an-ip-address/">What is an IP address?</a>
            <a href="http://css-tricks.com/dom/">The DOM Explained</a> *** (Note, do not worry about DOM manipulation at this time)
            <a href="http://www.html5rocks.com/en/tutorials/internals/howbrowserswork">How Browsers Work</a>
            <a href="http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url">What happens when click a URL?</a></p>
    
        <h4>Download In-Class Example:</h4>
        <p><a href="docs/OWLJan-24-14PowerPoint.pptx">LECTURE POWER POINT</a>
            <a href="classExample/class2-eg/class2-eg.zip">class2-eg.zip</a></p>
        
        <h4>Screencast RECAP session:</h4>
        <p>(Currently Unavailable)</p>        
'''

class03 = '''
        <h3>Class 3: Jan 24</h3>
        
        <h4>Due:</h4>
        <p>N/A, however recommended you have some sort of list with links your site will use.</p>
        
        <h4>Homework:</h4>
        <p>Modify the nav/menu and think about how to organize portfolio website (with JS and animation, minimalism, multiple pages, etc.)</p>
        
        <h4>Summary</h4>
        <ol>
            <li>Crash course to CSS (see Power Point below)</li>
            <li>Tutorial on how to make various navigation bars, such as
                <ul>
                    <li>Mimic Twitter bootstrap</li>
                    <li>DropDown menu Navigation</li>
                </ul></li>
        </ol>
        
        <h4>Few decent CSS guides:</h4>
        <p><a href="http://css-tricks.com/snippets/">CSS Tricks</a>
            <a href="http://line25.com/">CSS Specific Tutorials</a>
            </p>
    
        <h4>Download In-Class Example:</h4>
        <p><a href="docs/OWLJan-28-14-CSS2Know.pptx">CSS POWER POINT</a>
            <a href="classExample/class3-eg/navStyles.zip">Example Navigation Bars</a></p>
        
        <h4>Screencast RECAP session:</h4>
        <p>(Currently Unavailable)</p>   
'''

class04 = '''
        <h3>Class 4: Jan 31</h3>
        
        <h4>Due:</h4>
        <p>Find 3 portfolio websites you like some element of (eg. navigation, project page, layout, etc.)</p>

        <h4>Homework:</h4>
        <p>Sketch a wireframe of your portfolio website.</p>
        
        <h4>Summary:</h4>
        <ol>
            <li>Went over wireframes, site maps, & content maps.</li>
            <li> Split up into teams of 3-4 people.
                <ul>
                    <li>Made wireframes & site maps of websites of choice</li>
                    <li>Presented website, its design, what it was, good/bad, etc.</li>
                </ul></li>
        </ol>

'''

class05 = '''
    <h3>Class 5: Feb 4</h3>
    
    <h4>Homework:</h4>
    <p>Wireframe Sketch</p>
    
'''


def generate():
    allClasses = [class01, class02, class03, class04, class05]
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