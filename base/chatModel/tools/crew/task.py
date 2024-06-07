from crewai import Task
from textwrap import dedent


class CourseContentTask:
    
    def __tip_selection(self):
        return "If you do your BEST WORK, I'll tip you $100!"
    
    def google_task(self, agent, course_query: str, current_level: str, desired_level: str):
        return Task(
            description=dedent(
                f"""
                Analyse and collate the best and most personalized course content possible based
                on specific criteria such as what skills user intends to learn, their current
                skills level and their expected skills level: what skills they intend to have 
                developed by the end of the course. when generating the course content, reason with 
                all the information available to you as well as your training data to generate the 
                course content. For the course modules, there shouldn't be any sub modules, each module should be a single
                relevant concept with which a course video and code notebook can be generated that will
                explain the module sufficiently. this means course modules can be up to 20 or more.
                {self.__tip_selection()}

        

                Given the following information:
                Course and language the user intends to learn: {course_query}
                User current level of expertise: {current_level}
                User desired level of expertise: {desired_level}
                """
            ),
            expected_output= """ Should be of the structure below, change the values.
                                ###
                    Course Name -- Enter course name

                    Course Definition -- Master the essentials of web development with HTML, CSS, and JavaScript on our interactive learning platform.

                    Course Description -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

                    Learning Objectives --
                    1. Create responsive and interactive web pages
                    2. Build and style web layouts
                    3. Manipulate the document object model
                    4. Collaborate using version control

                    Timeline -- 4 Months

                    Recommended Experience -- Beginner Level

                    Tools Needed -- Laptop

                    Course Content
                    1. Module One Name: Introduction to Wireframe
                    Module One Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    2. Module Two Name: Introduction to HTML tags
                    Module Two Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    [continuation for as many modules]
                    ###
                                """,
            agent=agent,
            async_execution=True
        )
    
    def bing_task(self, agent, course_query: str, current_level: str, desired_level: str):
        return Task(
            description=dedent(
                f"""
                Analyse and collate the best and most personalized course content possible based
                on specific criteria such as what skills user intends to learn, their current
                skills level and their expected skills level: what skills they intend to have 
                developed by the end of the course. when generating the course content, reason with 
                all the information available to you as well as your training data to generate the 
                course content. For the course modules, there shouldn't be any sub modules, each module should be a single
                relevant concept with which a course video and code notebook can be generated that will
                explain the module sufficiently. this means course modules can be up to 20 or more.
                {self.__tip_selection()}

        

                Given the following information:
                Course and language the user intends to learn: {course_query}
                User current level of expertise: {current_level}
                User desired level of expertise: {desired_level}
                """
            ),
            expected_output= """ Should be of the structure below, change the values.
                                ###
                    Course Name -- Enter course name

                    Course Definition -- Master the essentials of web development with HTML, CSS, and JavaScript on our interactive learning platform.

                    Course Description -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

                    Learning Objectives --
                    1. Create responsive and interactive web pages
                    2. Build and style web layouts
                    3. Manipulate the document object model
                    4. Collaborate using version control

                    Timeline -- 4 Months

                    Recommended Experience -- Beginner Level

                    Tools Needed -- Laptop

                    Course Content
                    1. Module One Name: Introduction to Wireframe
                    Module One Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    2. Module Two Name: Introduction to HTML tags
                    Module Two Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    [continuation for as many modules]
                    ###
                                """,
            agent=agent,
            async_execution=True
        )
    
    def combine_task(self, agent, course_query, current_level, desired_level, context):
        return Task(description=dedent(
            f"""
            use the information at your disposal as well as your training data to collate the 
            best course content that addresses the course information and programming language,
            current skills level of the user and desired skills level of the user as provided below.
            {self.__tip_selection()}

            Given the following information:
                Course and language the user intends to learn: {course_query}
                User current level of expertise: {current_level}
                User desired level of expertise: {desired_level}

            Output must be a valid JSON object having the specified keys.
            """
        ),
        expected_output="""
                    Should be a valid JSON object with the following keys:
                                ###
                    Course Name -- Enter course name

                    Course Definition -- Master the essentials of web development with HTML, CSS, and JavaScript on our interactive learning platform.

                    Course Description -- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

                    Learning Objectives --
                    1. Create responsive and interactive web pages
                    2. Build and style web layouts
                    3. Manipulate the document object model
                    4. Collaborate using version control

                    Timeline -- 4 Months

                    Recommended Experience -- Beginner Level

                    Tools Needed -- Laptop

                    Course Content
                    1. Module One Name: Introduction to Wireframe
                    Module One Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    2. Module Two Name: Introduction to HTML tags
                    Module Two Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                    [continuation for as many modules]
                    ###
                                
                        """,
        agent=agent,
        async_execution=True,
        context=context
        )
