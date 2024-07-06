from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def message_summary(message:str) -> (str):
    result = summarizer(message, max_length=30, do_sample=False)
    summary = result[0]['summary_text']
    return summary

if __name__ == "__main__":
    ARTICLE = " I am trying to solve many problems of my business. The goals of the app is I want to market my salon. So anyone who knows the name of my salon can browse and checkout what we offer. and also rather than showing up all of a sudden to get services or calling all the time and scheduling or coming to the salon to schedule, I think it will be easier if we can let them book appointments before coming to the salon. Even without booking they can come, but they may have to leave if we're not available when they're coming. So we want to solve that problem by letting them book online. and also they will be able to see the things we offer. That way rather than depending on what they've heard or making call all the time, they can checkout our website"

    # "I am trying to solve many problems of my business. The goals of the app is I want to market my salon. So anyone who knows the name of my salon can browse and checkout what we offer. and also rather than showing up all of a sudden to get services or calling all the time and scheduling or coming to the salon to schedule, I think it will be easier if we can let them book appointments before coming to the salon. Even without booking they can come, but they may have to leave if we're not available when they're coming. So we want to solve that problem by letting them book online. and also they will be able to see the things we offer. That way rather than depending on what they've heard or making call all the time, they can checkout our website"
    # "I want to let the users book appointments by giving their convenient date and time as an input. You can let them chose through a calendar and time selector or just as an input, anyway you like. There is no need to consider our employee availability, users just have to input date, time. NIC number and email so that we can contact them regarding the appointment."
    print(f"Summary: {message_summary(ARTICLE)}")
