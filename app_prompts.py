prompt_template_1 = """
  You will be provide to compare multiple documentations in form of chunks, if asked to compare, then check the equivalent information from both documentation and provide the accurate results.
  Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
  provided context just say, "Ask different Question", don't provide the wrong answer\n\n
  Context:\n {context}?\n
  Question: \n{question}\n
  """