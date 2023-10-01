import wordcloud
from typing import List,Dict,Any
from . import cut

def countWords(content:List[str])->Dict[str,int]:
    result:Dict[str,int]={}
    for i in content:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    return result

def generateWc(content,*args,**kw):
    """
    Generates a word cloud based on the given content.

    Parameters:
    - content: A string or a list. If a string is provided, it will be processed using the default word cutting method. If a list is provided, it will be used to count the frequency of each word.

    Optional Parameters:
    - args: Additional arguments to be passed to the word cloud generator.
    - kw: Additional keyword arguments to be passed to the word cloud generator.

    Returns:
    - None
    """
    if isinstance(content,str):
        content=cut.cutWordDefault(content)
    if isinstance(content,list):
        content=countWords(content)
    wc=wordcloud.WordCloud(*args,**kw)
    wc.generate_from_frequencies(content)
    return wc


def generate(content,toFile,*args,**kw):
    """
    Generates a file from the given content and saves it to the specified location.

    Args:
        content (str): The content to generate the file from.
        toFile (str): The file path to save the generated file to.
        *args: Additional arguments to be passed to the word cloud generator.
        **kw: Additional keyword arguments to be passed to the word cloud generator.

    Returns:
        None
    """
    generateWc(content,*args,**kw).to_file(toFile)