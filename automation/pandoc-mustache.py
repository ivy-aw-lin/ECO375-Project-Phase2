"""
Pandoc filter to apply mustache templates on regular text.
"""
from panflute import *
import pystache, yaml

def prepare(doc):
    """ Parse metadata to obtain list of mustache templates,
        then load those templates.
    """
    doc.mustache_files = doc.get_metadata('mustache')
    doc.mustache_files = [' '.join(file.split()) for file in doc.mustache_files] # normalize whitespace characters
    if isinstance(doc.mustache_files, str):  # process single YAML value stored as string
        if not doc.mustache_files:
            doc.mustache_files = None  # switch empty string back to None
        else:
            doc.mustache_files = [ doc.mustache_files ]  # put non-empty string in list
    # with open('debug.txt', 'a') as the_file:
    #     the_file.write(str(doc.mustache_files))
    #     the_file.write('\n')
    if doc.mustache_files is not None:
        # Safely load YAML files and filter out any that fail to load or are None
        doc.mustache_hashes = []
        for file in doc.mustache_files:
            content = yaml.load(open(file, 'r').read(), Loader=yaml.SafeLoader)
            if isinstance(content, dict):
                doc.mustache_hashes.append(content)

        # Combine list of dicts into a single dict
        doc.mhash = { k: v for mdict in doc.mustache_hashes for k, v in mdict.items() }

        # Set up the Mustache renderer
        doc.mrenderer = pystache.Renderer(escape=lambda u: u, missing_tags='ignore')
    else:
        doc.mhash = None

def action(elem, doc):
    """ Apply combined mustache template to all strings in document.
    """
    if type(elem) in (Str, Math, CodeBlock, Code, RawBlock) and doc.mhash is not None:
        elem.text = doc.mrenderer.render(elem.text, doc.mhash)
        return elem

def main(doc=None):
    return run_filter(action, prepare=prepare, doc=doc)

if __name__ == '__main__':
    main()
