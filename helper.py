# helper.py

def run_code(language, code):
    """
    Function to simulate running code.
    لاحقًا يمكنكِ تطويرها لتشغيل لغات مختلفة.
    """
    if language == "python":
        try:
            exec_globals = {}
            exec(code, exec_globals)
            return exec_globals
        except Exception as e:
            return {"error": str(e)}

    return {"error": "Language not supported yet"}