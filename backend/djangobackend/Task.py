from crewai import Task


class Tasks:
    def MathematicsTask(self, agent):
        return Task(
            description=f"""Find the latest English medium syllabus for the subject of Mathematics in India as maximum as you want.Please provied for 2023.""",
            expected_output=f"""A bullet list summary of the all syllabus only.""",
            agent=agent,
            output_file="Mathematics.md",
        )

    def DetailOfChapterInMathematicsTask(self, agent, MathematicsTask):
        return Task(
            description=f""" Please ensure that you provide results for finding the latest detailed explanation of the English medium chapter for Mathematics in India.
            Give a big description like every chapter overview . Also give some sample question and answer. 
            I want to provide my students with study materials that will make them happy.""",
            expected_output=f"""A bullet list summary of the all those chapter with description""",
            agent=agent,
            context=[MathematicsTask],
            output_file="MathematicsChapter.md",
        )

    def EnglishTask(self, agent):
        return Task(
            description="""Find the latest English medium syllabus for the subject of English in India as maximum as you want.Please provied for 2023.""",
            expected_output=f"""A bullet list summary of the all syllabus """,
            agent=agent,
            output_file="English.md",
        )

    def DetailOfChapterInEnglishTask(self, agent, EnglishTask):
        return Task(
            description=f"""Please ensure that you provide results for finding the latest detailed explanation of the English medium chapter for English in India.
            Give a big description like chapter overview. Also give some sample question and answer. 
            I want to provide my students with study materials that will make them happy""",
            expected_output=f"""A bullet list summary of the all those chapter with description and also sample question and answer.""",
            agent=agent,
            context=[EnglishTask],
            output_file="EnglishChapter.md",
        )

    def ScienceTask(self, agent):
        return Task(
            description=f"""  Find the latest English medium syllabus for the subject of Science in India as maximum as you want.Please provied for 2023.""",
            expected_output=f"""A bullet list summary of the all syllabus .""",
            output_file="Science.md",
            agent=agent,
        )

    def DetailOfChapterInScienceTask(self, agent, ScienceTask):
        return Task(
            description=f""" Please ensure that you provide results for finding the latest detailed explanation of the English medium chapter for Science in India.
            Give a big description like chapter overview.Also give some sample question and answer. """,
            expected_output=f"""A bullet list summary of the all those chapter with description and also sample question and answer.
            I want to provide my students with study materials that will make them happy.""",
            agent=agent,
            context=[ScienceTask],
            output_file="ScienceChapter.md",
        )

    def HistoryTask(self, agent):
        return Task(
            description=f"""Find the latest English medium syllabus for the subject of History in India as maximum as you want.Please provied for 2023.""",
            expected_output=f"""A bullet list summary of the all syllabus """,
            agent=agent,
            output_file="History.md",
        )

    def DetailOfChapterInHistoryTask(self, agent, HistoryTask):
        return Task(
            description=f""" Please ensure that you provide results for finding the latest detailed explanation of the English medium chapter for History in India.
            Give a big description like chapter overview. Also give some sample question and answer.
            I want to provide my students with study materials that will make them happy.""",
            expected_output=f"""A bullet list summary of the all those chapter with description and also sample question and answer.""",
            agent=agent,
            context=[HistoryTask],
            output_file="HistoryChapter.md",
        )

    def GeographyTask(self, agent):
        return Task(
            description=""" Find the latest English medium syllabus for the subject of Geography in India as maximum as you want.Please provied for 2023.""",
            expected_output=f"""A bullet list summary of the all syllabus """,
            agent=agent,
            output_file="Geography.md",
        )

    def DetailOfChapterInGeographyTask(self, agent, GeographyTask):
        return Task(
            description=f"""Please ensure that you provide results for finding the latest detailed explanation of the English medium chapter for Geography in India.
            Give a big description like chapter overview. Also give some sample question and answer.
            I want to provide my students with study materials that will make them happy.""",
            expected_output=f"""A bullet list summary of the all those chapter with description and also sample question and answer.""",
            agent=agent,
            context=[GeographyTask],
            output_file="GeographyChapter.md",
        )
