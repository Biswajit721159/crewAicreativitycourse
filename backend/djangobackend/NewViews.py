from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key
from djangobackend.NewTask import NewTasks
from djangobackend.NewAgent import NewAgents
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from djangobackend.Openaicall import TestToGiveChatgpt


@csrf_exempt
async def Excute(request):
    try:
        SubjectAgent = NewAgents().SubjectAgent()
        SubjectTask = NewTasks().SubjectTask(SubjectAgent)

        crew = Crew(
            agents=[
                SubjectAgent,
            ],
            tasks=[
                SubjectTask,
            ],
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model="gpt-4-turbo"),
        )
        result = crew.kickoff()
        result = await TestToGiveChatgpt(result)
        if isinstance(result, list):
            for subject in result:
                await CallToCrewAi(subject)
        return JsonResponse(result, safe=False)

    except Exception as error:
        print("Error is ok ######### ", error)
        return JsonResponse(
            [
                {
                    "ConnectToDataBaseOutput": "Your maximum context is reached or your query is invalid. Please refresh this page and write your query again."
                }
            ],
            safe=False,
        )


@csrf_exempt
async def CallToCrewAi(Subject):
    try:
        ChapterAgent = NewAgents().ChapterAgent(Subject)
        TopicAgent = NewAgents().TopicAgent()
        SubtopicAgent = NewAgents().SubtopicAgent()
        ContentDevelopmentAgent = NewAgents().ContentDevelopmentAgent()
        AssessmentGenerationAgent = NewAgents().AssessmentGenerationAgent()
        ReviewandAdjustmentAgent = NewAgents().ReviewandAdjustmentAgent()

        ChapterTask = NewTasks().ChapterTask(ChapterAgent, Subject)
        TopicTask = NewTasks().TopicTask(TopicAgent, ChapterTask, Subject)
        SubtopicTask = NewTasks().SubtopicTask(SubtopicAgent, TopicTask, Subject)
        ContentDevelopmentTask = NewTasks().ContentDevelopmentTask(
            ContentDevelopmentAgent, SubtopicTask, Subject
        )
        AssessmentGenerationTask = NewTasks().AssessmentGenerationTask(
            AssessmentGenerationAgent, ContentDevelopmentTask, Subject
        )
        ReviewandAdjustmentTask = NewTasks().ReviewandAdjustmentTask(
            ReviewandAdjustmentAgent, AssessmentGenerationTask, Subject
        )

        crew = Crew(
            agents=[
                ChapterAgent,
                TopicAgent,
                SubtopicAgent,
                ContentDevelopmentAgent,
                AssessmentGenerationAgent,
                ReviewandAdjustmentAgent,
            ],
            tasks=[
                ChapterTask,
                TopicTask,
                SubtopicTask,
                ContentDevelopmentTask,
                AssessmentGenerationTask,
                ReviewandAdjustmentTask,
            ],
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model="gpt-4-turbo"),
        )
        result = crew.kickoff()
        return JsonResponse(result, safe=False)
    except Exception as error:
        print(error)
        pass


current_directory = os.path.dirname(os.path.abspath(__file__))
backendcode_directory = os.path.dirname(current_directory)


async def FrontendCode():
    markdown_file_path = os.path.join(backendcode_directory, "frontendcode.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    return markdown_content


async def BackendCode():
    markdown_file_path = os.path.join(backendcode_directory, "Backendoutput.md")
    with open(markdown_file_path, "r") as f:
        markdown_content = f.read()
    return markdown_content


def solve(string):

    ans = []
    # start
    ans.append({"code": string})
    return ans
    # end
    n = len(string)
    word = ""
    i = 0
    while i < n:
        if (
            i + 2 < n
            and string[i] == "`"
            and string[i + 1] == "`"
            and string[i + 2] == "`"
        ):
            ans.append({"text": word})
            word = ""
            j = i + 3
            while j < n:
                if (
                    j + 2 < n
                    and string[j] == "`"
                    and string[j + 1] == "`"
                    and string[j + 2] == "`"
                ):
                    ans.append({"code": word})
                    i = j + 2
                    word = ""
                    break
                else:
                    word += string[j]
                j += 1
        else:
            word += string[i]
        i += 1

    if len(word) != 0:
        ans.append({"text": word})

    return ans
