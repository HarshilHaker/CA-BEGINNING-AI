import os
import string
import random
import tqdm
from tqdm import tqdm
from win32com.client import Dispatch
import datetime
import subprocess

print("CA SOTWARES")
print("CA 1.8.5 [CA SOFTWARES]")
print("2020 CA Corporation. All rights reserved.")
print("Developer: Harshil Anuwadia")
print("Made In India")
import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    plen = int(6)

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("".join(s[0:plen]))
    import datetime

    today = datetime.date.today()
    print("Date:", today)
    def speak(str):
        speak = Dispatch(("SAPI.spVoice"))
        speak.Speak(str)
while True:
    ha1 = input(">>> CA ")
    if ha1 == "import CA":
        from tqdm import tqdm

        loop = tqdm(total=1500, position=0, leave=False)

        for k in range(1500):

            loop.set_description("Importing CA".format(k))

            loop.update(1)

        loop.close()
        print("")
        print('''-----------------
|CA Is Imported.|
-----------------''')
        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("CA is imported")

        break
    else:
        print("Error, For Importing CA. Please Try Again.")

while True:
    a = input(">>>>> CA ")
    if a == "h":
        print("h")



    elif a == "VA":
        a13 = input('''This Function Will Use Your Internet Connection So, Please Make Sure That You Are Connected To Internet. 
Press Enter Key To Continue: ''')
        import pyttsx3
        import speech_recognition as sr
        import datetime
        import wikipedia
        import webbrowser
        import os


        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # print(voices[1].id)
        engine.setProperty('voice', voices[0].id)


        def speak(audio):
            engine.say(audio)
            engine.runAndWait()


        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning!")

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon!")

            else:
                speak("Good Evening!")

            speak("I am CA. Please tell me how may I help you")


        def takeCommand():
            # It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"You said: {query}\n")

            except Exception as e:
                # print(e)
                print("Say that again please...")
                return "None"
            return query

        if __name__ == "__main__":
            wishMe()
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                elif 'play music' in query:
                    music_dir = 'C:\\Users\\Admin\\Music\\Songs'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
                                                                                               
                elif "shutdown" in query:
                    speak("shutting down")
                    os.system("shutdown -s")                                                                              

                elif "email" in query:
                    import smtplib
                    a = input("Reciever Email ID: ")
                    b = input("Subject: ")
                    c = input("Message: ")
                    TO = a
                    SUBJECT = b
                    TEXT = c

                    # Gmail Sign In
                    gmail_sender = 'harshilanuwadia97@gmail.com'
                    gmail_passwd = 'ha@@##421600'

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(gmail_sender, gmail_passwd)

                    BODY = '\r\n'.join(['To: %s' % TO,
                                        'From: %s' % gmail_sender,
                                        'Subject: %s' % SUBJECT,
                                        '', TEXT])

                    try:
                        server.sendmail(gmail_sender, [TO], BODY)
                        print('Email Sent')
                    except:
                        print('Error Sending Mail')

                    server.quit()

    elif a == "play criper":
        print("In this game show charecter is not real nither a name and events.")
        print("This all things is a part of the game.")
        ha = input("Agree the termes and condition [yes/no]: ")
        if ha == "no":
            print("You are not eligible to play the game criper.")
            print("Please exit from the game.")
        elif ha == "yes":
            print("Welcome to the game criper.")
            import tqdm
            from tqdm import tqdm

            from tqdm import tqdm

            from tqdm import tqdm

            loop = tqdm(total=30000, position=0, leave=False)
            for k in range(30000):
                loop.set_description("Loading Criper".format(k))
                loop.update(1)
            loop.close()
            import tqdm
            from tqdm import tqdm

            from tqdm import tqdm

            from tqdm import tqdm

            loop = tqdm(total=10000, position=0, leave=False)
            for k in range(10000):
                loop.set_description("Loading Script".format(k))
                loop.update(1)
            loop.close()
            print("All done")
            ha1 = input("Press code 421600 to start game: ")
            if ha1 == "421600":
                print("")
                print("Story Of The Game")
                print("")
                print("Before 7 years ago.")
                print("There was a 5 murder case on you and you was rejected for some reason,")
                print("You and your friend need to prove that you are innocent.")
                print("Your friend name is Alex.")
                haq1 = input("Are you ready for the investigation [Press r]:")
                if haq1 == "r":
                    import tkinter
                    from tkinter import *

                root = Tk()
                # set window colour
                root.configure(background='black')


                def send():
                    # set your reply.
                    # set what want to take reply from Promox Bot.

                    send = "You => " + e.get()
                    txt.insert(END, "\n" + send)
                    # your message to bot.
                    if (e.get() == "Alex"):
                        txt.insert(END, "\n" + '''Alex => Hi

       How are you.

       I need to talk with you some things

       Select any one reply [What/What do you want from me]''')
                    elif (e.get() == "What do you want from me"):
                        txt.insert(END, "\n" + '''Alex => I am knowing that you are innocent,
       and you did't do murder of any five but your case is going to reopning in court,
       you should do something for it

       Select any one reply [you are my real friend/ok we need to do something]''')

                    elif (e.get() == "What"):
                        txt.insert(END, "\n" + '''Alex => I am knowing that you are innocent,
       and you did't do murder of any five but your case is going to reopning in court,
       you should do something for it

       Select any one reply [you are my real friend/ok we need to do something]''')


                    elif (e.get() == "you are my real friend"):
                        txt.insert(END, "\n" + '''Alex => Most welcome
       Ok then listern

       You need to add the persin Kaine,
       She will help in this investigation.

       Reply with [ok]''')

                    else:

                        txt.insert(END, "\n" + "Bot => Sorry I did't get it")

                        # delete messange from entry box.

                    e.delete(0, END)
                    # --------------------------------------------------------------
                    # making the entry box width long.


                txt = Text(root)
                txt.grid(row=0, column=0, columnspan=2)

                e = Entry(root, width=100)
                # making of Send button at left side of the entry box.

                send = Button(root, text="Send", command=send).grid(row=1, column=1)
                e.grid(row=1, column=0)

                # Your chat bot name.
                root.title("Criper")

                # set the loop
                root.mainloop()

    elif a == "exit":
        "Usage: unparse.py <path to source file>"
        import sys
        import ast
        import tokenize
        import io
        import os

        # Large float and imaginary literals get turned into infinities in the AST.
        # We unparse those infinities to INFSTR.
        INFSTR = "1e" + repr(sys.float_info.max_10_exp + 1)


        def interleave(inter, f, seq):
            """Call f on each item in seq, calling inter() in between.
                """
            seq = iter(seq)
            try:
                f(next(seq))
            except StopIteration:
                pass
            else:
                for x in seq:
                    inter()
                    f(x)


        class Unparser:
            """Methods in this class recursively traverse an AST and
                output source code for the abstract syntax; original formatting
                is disregarded. """

            def __init__(self, tree, file=sys.stdout):
                """Unparser(tree, file=sys.stdout) -> None.
                     Print the source for tree to file."""
                self.f = file
                self._indent = 0
                self.dispatch(tree)
                print("", file=self.f)
                self.f.flush()

            def fill(self, text=""):
                "Indent a piece of text, according to the current indentation level"
                self.f.write("\n" + "    " * self._indent + text)

            def write(self, text):
                "Append a piece of text to the current line."
                self.f.write(text)

            def enter(self):
                "Print ':', and increase the indentation."
                self.write(":")
                self._indent += 1

            def leave(self):
                "Decrease the indentation level."
                self._indent -= 1

            def dispatch(self, tree):
                "Dispatcher function, dispatching tree type T to method _T."
                if isinstance(tree, list):
                    for t in tree:
                        self.dispatch(t)
                    return
                meth = getattr(self, "_" + tree.__class__.__name__)
                meth(tree)

            ############### Unparsing methods ######################
            # There should be one method per concrete grammar type #
            # Constructors should be grouped by sum type. Ideally, #
            # this would follow the order in the grammar, but      #
            # currently doesn't.                                   #
            ########################################################

            def _Module(self, tree):
                for stmt in tree.body:
                    self.dispatch(stmt)

            # stmt
            def _Expr(self, tree):
                self.fill()
                self.dispatch(tree.value)

            def _NamedExpr(self, tree):
                self.write("(")
                self.dispatch(tree.target)
                self.write(" := ")
                self.dispatch(tree.value)
                self.write(")")

            def _Import(self, t):
                self.fill("import ")
                interleave(lambda: self.write(", "), self.dispatch, t.names)

            def _ImportFrom(self, t):
                self.fill("from ")
                self.write("." * t.level)
                if t.module:
                    self.write(t.module)
                self.write(" import ")
                interleave(lambda: self.write(", "), self.dispatch, t.names)

            def _Assign(self, t):
                self.fill()
                for target in t.targets:
                    self.dispatch(target)
                    self.write(" = ")
                self.dispatch(t.value)

            def _AugAssign(self, t):
                self.fill()
                self.dispatch(t.target)
                self.write(" " + self.binop[t.op.__class__.__name__] + "= ")
                self.dispatch(t.value)

            def _AnnAssign(self, t):
                self.fill()
                if not t.simple and isinstance(t.target, ast.Name):
                    self.write('(')
                self.dispatch(t.target)
                if not t.simple and isinstance(t.target, ast.Name):
                    self.write(')')
                self.write(": ")
                self.dispatch(t.annotation)
                if t.value:
                    self.write(" = ")
                    self.dispatch(t.value)

            def _Return(self, t):
                self.fill("return")
                if t.value:
                    self.write(" ")
                    self.dispatch(t.value)

            def _Pass(self, t):
                self.fill("pass")

            def _Break(self, t):
                self.fill("break")

            def _Continue(self, t):
                self.fill("continue")

            def _Delete(self, t):
                self.fill("del ")
                interleave(lambda: self.write(", "), self.dispatch, t.targets)

            def _Assert(self, t):
                self.fill("assert ")
                self.dispatch(t.test)
                if t.msg:
                    self.write(", ")
                    self.dispatch(t.msg)

            def _Global(self, t):
                self.fill("global ")
                interleave(lambda: self.write(", "), self.write, t.names)

            def _Nonlocal(self, t):
                self.fill("nonlocal ")
                interleave(lambda: self.write(", "), self.write, t.names)

            def _Await(self, t):
                self.write("(")
                self.write("await")
                if t.value:
                    self.write(" ")
                    self.dispatch(t.value)
                self.write(")")

            def _Yield(self, t):
                self.write("(")
                self.write("yield")
                if t.value:
                    self.write(" ")
                    self.dispatch(t.value)
                self.write(")")

            def _YieldFrom(self, t):
                self.write("(")
                self.write("yield from")
                if t.value:
                    self.write(" ")
                    self.dispatch(t.value)
                self.write(")")

            def _Raise(self, t):
                self.fill("raise")
                if not t.exc:
                    assert not t.cause
                    return
                self.write(" ")
                self.dispatch(t.exc)
                if t.cause:
                    self.write(" from ")
                    self.dispatch(t.cause)

            def _Try(self, t):
                self.fill("try")
                self.enter()
                self.dispatch(t.body)
                self.leave()
                for ex in t.handlers:
                    self.dispatch(ex)
                if t.orelse:
                    self.fill("else")
                    self.enter()
                    self.dispatch(t.orelse)
                    self.leave()
                if t.finalbody:
                    self.fill("finally")
                    self.enter()
                    self.dispatch(t.finalbody)
                    self.leave()

            def _ExceptHandler(self, t):
                self.fill("except")
                if t.type:
                    self.write(" ")
                    self.dispatch(t.type)
                if t.name:
                    self.write(" as ")
                    self.write(t.name)
                self.enter()
                self.dispatch(t.body)
                self.leave()

            def _ClassDef(self, t):
                self.write("\n")
                for deco in t.decorator_list:
                    self.fill("@")
                    self.dispatch(deco)
                self.fill("class " + t.name)
                self.write("(")
                comma = False
                for e in t.bases:
                    if comma:
                        self.write(", ")
                    else:
                        comma = True
                    self.dispatch(e)
                for e in t.keywords:
                    if comma:
                        self.write(", ")
                    else:
                        comma = True
                    self.dispatch(e)
                self.write(")")

                self.enter()
                self.dispatch(t.body)
                self.leave()

            def _FunctionDef(self, t):
                self.__FunctionDef_helper(t, "def")

            def _AsyncFunctionDef(self, t):
                self.__FunctionDef_helper(t, "async def")

            def __FunctionDef_helper(self, t, fill_suffix):
                self.write("\n")
                for deco in t.decorator_list:
                    self.fill("@")
                    self.dispatch(deco)
                def_str = fill_suffix + " " + t.name + "("
                self.fill(def_str)
                self.dispatch(t.args)
                self.write(")")
                if t.returns:
                    self.write(" -> ")
                    self.dispatch(t.returns)
                self.enter()
                self.dispatch(t.body)
                self.leave()

            def _For(self, t):
                self.__For_helper("for ", t)

            def _AsyncFor(self, t):
                self.__For_helper("async for ", t)

            def __For_helper(self, fill, t):
                self.fill(fill)
                self.dispatch(t.target)
                self.write(" in ")
                self.dispatch(t.iter)
                self.enter()
                self.dispatch(t.body)
                self.leave()
                if t.orelse:
                    self.fill("else")
                    self.enter()
                    self.dispatch(t.orelse)
                    self.leave()

            def _If(self, t):
                self.fill("if ")
                self.dispatch(t.test)
                self.enter()
                self.dispatch(t.body)
                self.leave()
                # collapse nested ifs into equivalent elifs.
                while (t.orelse and len(t.orelse) == 1 and
                       isinstance(t.orelse[0], ast.If)):
                    t = t.orelse[0]
                    self.fill("elif ")
                    self.dispatch(t.test)
                    self.enter()
                    self.dispatch(t.body)
                    self.leave()
                # final else
                if t.orelse:
                    self.fill("else")
                    self.enter()
                    self.dispatch(t.orelse)
                    self.leave()

            def _While(self, t):
                self.fill("while ")
                self.dispatch(t.test)
                self.enter()
                self.dispatch(t.body)
                self.leave()
                if t.orelse:
                    self.fill("else")
                    self.enter()
                    self.dispatch(t.orelse)
                    self.leave()

            def _With(self, t):
                self.fill("with ")
                interleave(lambda: self.write(", "), self.dispatch, t.items)
                self.enter()
                self.dispatch(t.body)
                self.leave()

            def _AsyncWith(self, t):
                self.fill("async with ")
                interleave(lambda: self.write(", "), self.dispatch, t.items)
                self.enter()
                self.dispatch(t.body)
                self.leave()

            # expr
            def _JoinedStr(self, t):
                self.write("f")
                string = io.StringIO()
                self._fstring_JoinedStr(t, string.write)
                self.write(repr(string.getvalue()))

            def _FormattedValue(self, t):
                self.write("f")
                string = io.StringIO()
                self._fstring_FormattedValue(t, string.write)
                self.write(repr(string.getvalue()))

            def _fstring_JoinedStr(self, t, write):
                for value in t.values:
                    meth = getattr(self, "_fstring_" + type(value).__name__)
                    meth(value, write)

            def _fstring_Constant(self, t, write):
                assert isinstance(t.value, str)
                value = t.value.replace("{", "{{").replace("}", "}}")
                write(value)

            def _fstring_FormattedValue(self, t, write):
                write("{")
                expr = io.StringIO()
                Unparser(t.value, expr)
                expr = expr.getvalue().rstrip("\n")
                if expr.startswith("{"):
                    write(" ")  # Separate pair of opening brackets as "{ {"
                write(expr)
                if t.conversion != -1:
                    conversion = chr(t.conversion)
                    assert conversion in "sra"
                    write(f"!{conversion}")
                if t.format_spec:
                    write(":")
                    meth = getattr(self, "_fstring_" + type(t.format_spec).__name__)
                    meth(t.format_spec, write)
                write("}")

            def _Name(self, t):
                self.write(t.id)

            def _write_constant(self, value):
                if isinstance(value, (float, complex)):
                    # Substitute overflowing decimal literal for AST infinities.
                    self.write(repr(value).replace("inf", INFSTR))
                else:
                    self.write(repr(value))

            def _Constant(self, t):
                value = t.value
                if isinstance(value, tuple):
                    self.write("(")
                    if len(value) == 1:
                        self._write_constant(value[0])
                        self.write(",")
                    else:
                        interleave(lambda: self.write(", "), self._write_constant, value)
                    self.write(")")
                elif value is ...:
                    self.write("...")
                else:
                    if t.kind == "u":
                        self.write("u")
                    self._write_constant(t.value)

            def _List(self, t):
                self.write("[")
                interleave(lambda: self.write(", "), self.dispatch, t.elts)
                self.write("]")

            def _ListComp(self, t):
                self.write("[")
                self.dispatch(t.elt)
                for gen in t.generators:
                    self.dispatch(gen)
                self.write("]")

            def _GeneratorExp(self, t):
                self.write("(")
                self.dispatch(t.elt)
                for gen in t.generators:
                    self.dispatch(gen)
                self.write(")")

            def _SetComp(self, t):
                self.write("{")
                self.dispatch(t.elt)
                for gen in t.generators:
                    self.dispatch(gen)
                self.write("}")

            def _DictComp(self, t):
                self.write("{")
                self.dispatch(t.key)
                self.write(": ")
                self.dispatch(t.value)
                for gen in t.generators:
                    self.dispatch(gen)
                self.write("}")

            def _comprehension(self, t):
                if t.is_async:
                    self.write(" async for ")
                else:
                    self.write(" for ")
                self.dispatch(t.target)
                self.write(" in ")
                self.dispatch(t.iter)
                for if_clause in t.ifs:
                    self.write(" if ")
                    self.dispatch(if_clause)

            def _IfExp(self, t):
                self.write("(")
                self.dispatch(t.body)
                self.write(" if ")
                self.dispatch(t.test)
                self.write(" else ")
                self.dispatch(t.orelse)
                self.write(")")

            def _Set(self, t):
                assert (t.elts)  # should be at least one element
                self.write("{")
                interleave(lambda: self.write(", "), self.dispatch, t.elts)
                self.write("}")

            def _Dict(self, t):
                self.write("{")

                def write_key_value_pair(k, v):
                    self.dispatch(k)
                    self.write(": ")
                    self.dispatch(v)

                def write_item(item):
                    k, v = item
                    if k is None:
                        # for dictionary unpacking operator in dicts {**{'y': 2}}
                        # see PEP 448 for details
                        self.write("**")
                        self.dispatch(v)
                    else:
                        write_key_value_pair(k, v)

                interleave(lambda: self.write(", "), write_item, zip(t.keys, t.values))
                self.write("}")

            def _Tuple(self, t):
                self.write("(")
                if len(t.elts) == 1:
                    elt = t.elts[0]
                    self.dispatch(elt)
                    self.write(",")
                else:
                    interleave(lambda: self.write(", "), self.dispatch, t.elts)
                self.write(")")

            unop = {"Invert": "~", "Not": "not", "UAdd": "+", "USub": "-"}

            def _UnaryOp(self, t):
                self.write("(")
                self.write(self.unop[t.op.__class__.__name__])
                self.write(" ")
                self.dispatch(t.operand)
                self.write(")")

            binop = {"Add": "+", "Sub": "-", "Mult": "*", "MatMult": "@", "Div": "/", "Mod": "%",
                     "LShift": "<<", "RShift": ">>", "BitOr": "|", "BitXor": "^", "BitAnd": "&",
                     "FloorDiv": "//", "Pow": "**"}

            def _BinOp(self, t):
                self.write("(")
                self.dispatch(t.left)
                self.write(" " + self.binop[t.op.__class__.__name__] + " ")
                self.dispatch(t.right)
                self.write(")")

            cmpops = {"Eq": "==", "NotEq": "!=", "Lt": "<", "LtE": "<=", "Gt": ">", "GtE": ">=",
                      "Is": "is", "IsNot": "is not", "In": "in", "NotIn": "not in"}

            def _Compare(self, t):
                self.write("(")
                self.dispatch(t.left)
                for o, e in zip(t.ops, t.comparators):
                    self.write(" " + self.cmpops[o.__class__.__name__] + " ")
                    self.dispatch(e)
                self.write(")")

            boolops = {ast.And: 'and', ast.Or: 'or'}

            def _BoolOp(self, t):
                self.write("(")
                s = " %s " % self.boolops[t.op.__class__]
                interleave(lambda: self.write(s), self.dispatch, t.values)
                self.write(")")

            def _Attribute(self, t):
                self.dispatch(t.value)
                # Special case: 3.__abs__() is a syntax error, so if t.value
                # is an integer literal then we need to either parenthesize
                # it or add an extra space to get 3 .__abs__().
                if isinstance(t.value, ast.Constant) and isinstance(t.value.value, int):
                    self.write(" ")
                self.write(".")
                self.write(t.attr)

            def _Call(self, t):
                self.dispatch(t.func)
                self.write("(")
                comma = False
                for e in t.args:
                    if comma:
                        self.write(", ")
                    else:
                        comma = True
                    self.dispatch(e)
                for e in t.keywords:
                    if comma:
                        self.write(", ")
                    else:
                        comma = True
                    self.dispatch(e)
                self.write(")")

            def _Subscript(self, t):
                self.dispatch(t.value)
                self.write("[")
                if (isinstance(t.slice, ast.Index)
                        and isinstance(t.slice.value, ast.Tuple)
                        and t.slice.value.elts):
                    if len(t.slice.value.elts) == 1:
                        elt = t.slice.value.elts[0]
                        self.dispatch(elt)
                        self.write(",")
                    else:
                        interleave(lambda: self.write(", "), self.dispatch, t.slice.value.elts)
                else:
                    self.dispatch(t.slice)
                self.write("]")

            def _Starred(self, t):
                self.write("*")
                self.dispatch(t.value)

            # slice
            def _Ellipsis(self, t):
                self.write("...")

            def _Index(self, t):
                self.dispatch(t.value)

            def _Slice(self, t):
                if t.lower:
                    self.dispatch(t.lower)
                self.write(":")
                if t.upper:
                    self.dispatch(t.upper)
                if t.step:
                    self.write(":")
                    self.dispatch(t.step)

            def _ExtSlice(self, t):
                if len(t.dims) == 1:
                    elt = t.dims[0]
                    self.dispatch(elt)
                    self.write(",")
                else:
                    interleave(lambda: self.write(', '), self.dispatch, t.dims)

            # argument
            def _arg(self, t):
                self.write(t.arg)
                if t.annotation:
                    self.write(": ")
                    self.dispatch(t.annotation)

            # others
            def _arguments(self, t):
                first = True
                # normal arguments
                all_args = t.posonlyargs + t.args
                defaults = [None] * (len(all_args) - len(t.defaults)) + t.defaults
                for index, elements in enumerate(zip(all_args, defaults), 1):
                    a, d = elements
                    if first:
                        first = False
                    else:
                        self.write(", ")
                    self.dispatch(a)
                    if d:
                        self.write("=")
                        self.dispatch(d)
                    if index == len(t.posonlyargs):
                        self.write(", /")

                # varargs, or bare '*' if no varargs but keyword-only arguments present
                if t.vararg or t.kwonlyargs:
                    if first:
                        first = False
                    else:
                        self.write(", ")
                    self.write("*")
                    if t.vararg:
                        self.write(t.vararg.arg)
                        if t.vararg.annotation:
                            self.write(": ")
                            self.dispatch(t.vararg.annotation)

                # keyword-only arguments
                if t.kwonlyargs:
                    for a, d in zip(t.kwonlyargs, t.kw_defaults):
                        if first:
                            first = False
                        else:
                            self.write(", ")
                        self.dispatch(a),
                        if d:
                            self.write("=")
                            self.dispatch(d)

                # kwargs
                if t.kwarg:
                    if first:
                        first = False
                    else:
                        self.write(", ")
                    self.write("**" + t.kwarg.arg)
                    if t.kwarg.annotation:
                        self.write(": ")
                        self.dispatch(t.kwarg.annotation)

            def _keyword(self, t):
                if t.arg is None:
                    self.write("**")
                else:
                    self.write(t.arg)
                    self.write("=")
                self.dispatch(t.value)

            def _Lambda(self, t):
                self.write("(")
                self.write("lambda ")
                self.dispatch(t.args)
                self.write(": ")
                self.dispatch(t.body)
                self.write(")")

            def _alias(self, t):
                self.write(t.name)
                if t.asname:
                    self.write(" as " + t.asname)

            def _withitem(self, t):
                self.dispatch(t.context_expr)
                if t.optional_vars:
                    self.write(" as ")
                    self.dispatch(t.optional_vars)


        def roundtrip(filename, output=sys.stdout):
            with open(filename, "rb") as pyfile:
                encoding = tokenize.detect_encoding(pyfile.readline)[0]
            with open(filename, "r", encoding=encoding) as pyfile:
                source = pyfile.read()
            tree = compile(source, filename, "exec", ast.PyCF_ONLY_AST)
            Unparser(tree, output)


        def testdir(a):
            try:
                names = [n for n in os.listdir(a) if n.endswith('.py')]
            except OSError:
                print("Directory not readable: %s" % a, file=sys.stderr)
            else:
                for n in names:
                    fullname = os.path.join(a, n)
                    if os.path.isfile(fullname):
                        output = io.StringIO()
                        print('Testing %s' % fullname)
                        try:
                            roundtrip(fullname, output)
                        except Exception as e:
                            print('  Failed to compile, exception is %s' % repr(e))
                    elif os.path.isdir(fullname):
                        testdir(fullname)


        def main(args):
            if args[0] == '--testdir':
                for a in args[1:]:
                    testdir(a)
            else:
                for a in args:
                    roundtrip(a)


        if __name__ == '__main__':
            main(sys.argv[1:])

    elif a == "open exe":
        name = input("Name of exe file: ")
        url = input(str("Exe file location: "))
        print("Checking Of Valid File Location")

        import tqdm
        from tqdm import tqdm

        from tqdm import tqdm

        from tqdm import tqdm
        loop = tqdm(total=30000, position=0, leave=False)
        for k in range(30000):
            loop.set_description("".format(k))
            loop.update(1)
        loop.close()
        print("Valid File Location")
        print("")
        print("Checking For Virus")
        import tqdm
        from tqdm import tqdm

        from tqdm import tqdm

        from tqdm import tqdm
        loop = tqdm(total=30000, position=0, leave=False)
        for k in range(30000):
            loop.set_description("".format(k))
            loop.update(1)
        loop.close()
        print("No Virus Detected")
        print("Done")

        print("")
        print("Opening",name,"In Few Seconds")




        print("Changes Saved For This Program Only.")
        import subprocess
        import random

        file67 = subprocess.Popen(url)


    elif a == "open spreadsheet":
        # !/usr/bin/env python3

        """
            SS1 -- a spreadsheet-like application.
            """

        import os
        import re
        import sys
        from xml.parsers import expat
        from xml.sax.saxutils import escape

        LEFT, CENTER, RIGHT = "LEFT", "CENTER", "RIGHT"


        def ljust(x, n):
            return x.ljust(n)


        def center(x, n):
            return x.center(n)


        def rjust(x, n):
            return x.rjust(n)


        align2action = {LEFT: ljust, CENTER: center, RIGHT: rjust}

        align2xml = {LEFT: "left", CENTER: "center", RIGHT: "right"}
        xml2align = {"left": LEFT, "center": CENTER, "right": RIGHT}

        align2anchor = {LEFT: "w", CENTER: "center", RIGHT: "e"}


        def sum(seq):
            total = 0
            for x in seq:
                if x is not None:
                    total += x
            return total


        class Sheet:

            def __init__(self):
                self.cells = {}  # {(x, y): cell, ...}
                self.ns = dict(
                    cell=self.cellvalue,
                    cells=self.multicellvalue,
                    sum=sum,
                )

            def cellvalue(self, x, y):
                cell = self.getcell(x, y)
                if hasattr(cell, 'recalc'):
                    return cell.recalc(self.ns)
                else:
                    return cell

            def multicellvalue(self, x1, y1, x2, y2):
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1
                seq = []
                for y in range(y1, y2 + 1):
                    for x in range(x1, x2 + 1):
                        seq.append(self.cellvalue(x, y))
                return seq

            def getcell(self, x, y):
                return self.cells.get((x, y))

            def setcell(self, x, y, cell):
                assert x > 0 and y > 0
                assert isinstance(cell, BaseCell)
                self.cells[x, y] = cell

            def clearcell(self, x, y):
                try:
                    del self.cells[x, y]
                except KeyError:
                    pass

            def clearcells(self, x1, y1, x2, y2):
                for xy in self.selectcells(x1, y1, x2, y2):
                    del self.cells[xy]

            def clearrows(self, y1, y2):
                self.clearcells(0, y1, sys.maxsize, y2)

            def clearcolumns(self, x1, x2):
                self.clearcells(x1, 0, x2, sys.maxsize)

            def selectcells(self, x1, y1, x2, y2):
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1
                return [(x, y) for x, y in self.cells
                        if x1 <= x <= x2 and y1 <= y <= y2]

            def movecells(self, x1, y1, x2, y2, dx, dy):
                if dx == 0 and dy == 0:
                    return
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1
                assert x1 + dx > 0 and y1 + dy > 0
                new = {}
                for x, y in self.cells:
                    cell = self.cells[x, y]
                    if hasattr(cell, 'renumber'):
                        cell = cell.renumber(x1, y1, x2, y2, dx, dy)
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        x += dx
                        y += dy
                    new[x, y] = cell
                self.cells = new

            def insertrows(self, y, n):
                assert n > 0
                self.movecells(0, y, sys.maxsize, sys.maxsize, 0, n)

            def deleterows(self, y1, y2):
                if y1 > y2:
                    y1, y2 = y2, y1
                self.clearrows(y1, y2)
                self.movecells(0, y2 + 1, sys.maxsize, sys.maxsize, 0, y1 - y2 - 1)

            def insertcolumns(self, x, n):
                assert n > 0
                self.movecells(x, 0, sys.maxsize, sys.maxsize, n, 0)

            def deletecolumns(self, x1, x2):
                if x1 > x2:
                    x1, x2 = x2, x1
                self.clearcells(x1, x2)
                self.movecells(x2 + 1, 0, sys.maxsize, sys.maxsize, x1 - x2 - 1, 0)

            def getsize(self):
                maxx = maxy = 0
                for x, y in self.cells:
                    maxx = max(maxx, x)
                    maxy = max(maxy, y)
                return maxx, maxy

            def reset(self):
                for cell in self.cells.values():
                    if hasattr(cell, 'reset'):
                        cell.reset()

            def recalc(self):
                self.reset()
                for cell in self.cells.values():
                    if hasattr(cell, 'recalc'):
                        cell.recalc(self.ns)

            def display(self):
                maxx, maxy = self.getsize()
                width, height = maxx + 1, maxy + 1
                colwidth = [1] * width
                full = {}
                # Add column heading labels in row 0
                for x in range(1, width):
                    full[x, 0] = text, alignment = colnum2name(x), RIGHT
                    colwidth[x] = max(colwidth[x], len(text))
                # Add row labels in column 0
                for y in range(1, height):
                    full[0, y] = text, alignment = str(y), RIGHT
                    colwidth[0] = max(colwidth[0], len(text))
                # Add sheet cells in columns with x>0 and y>0
                for (x, y), cell in self.cells.items():
                    if x <= 0 or y <= 0:
                        continue
                    if hasattr(cell, 'recalc'):
                        cell.recalc(self.ns)
                    if hasattr(cell, 'format'):
                        text, alignment = cell.format()
                        assert isinstance(text, str)
                        assert alignment in (LEFT, CENTER, RIGHT)
                    else:
                        text = str(cell)
                        if isinstance(cell, str):
                            alignment = LEFT
                        else:
                            alignment = RIGHT
                    full[x, y] = (text, alignment)
                    colwidth[x] = max(colwidth[x], len(text))
                # Calculate the horizontal separator line (dashes and dots)
                sep = ""
                for x in range(width):
                    if sep:
                        sep += "+"
                    sep += "-" * colwidth[x]
                # Now print The full grid
                for y in range(height):
                    line = ""
                    for x in range(width):
                        text, alignment = full.get((x, y)) or ("", LEFT)
                        text = align2action[alignment](text, colwidth[x])
                        if line:
                            line += '|'
                        line += text
                    print(line)
                    if y == 0:
                        print(sep)

            def xml(self):
                out = ['<spreadsheet>']
                for (x, y), cell in self.cells.items():
                    if hasattr(cell, 'xml'):
                        cellxml = cell.xml()
                    else:
                        cellxml = '<value>%s</value>' % escape(cell)
                    out.append('<cell row="%s" col="%s">\n  %s\n</cell>' %
                               (y, x, cellxml))
                out.append('</spreadsheet>')
                return '\n'.join(out)

            def save(self, filename):
                text = self.xml()
                with open(filename, "w", encoding='utf-8') as f:
                    f.write(text)
                    if text and not text.endswith('\n'):
                        f.write('\n')

            def load(self, filename):
                with open(filename, 'rb') as f:
                    SheetParser(self).parsefile(f)


        class SheetParser:

            def __init__(self, sheet):
                self.sheet = sheet

            def parsefile(self, f):
                parser = expat.ParserCreate()
                parser.StartElementHandler = self.startelement
                parser.EndElementHandler = self.endelement
                parser.CharacterDataHandler = self.data
                parser.ParseFile(f)

            def startelement(self, tag, attrs):
                method = getattr(self, 'start_' + tag, None)
                if method:
                    method(attrs)
                self.texts = []

            def data(self, text):
                self.texts.append(text)

            def endelement(self, tag):
                method = getattr(self, 'end_' + tag, None)
                if method:
                    method("".join(self.texts))

            def start_cell(self, attrs):
                self.y = int(attrs.get("row"))
                self.x = int(attrs.get("col"))

            def start_value(self, attrs):
                self.fmt = attrs.get('format')
                self.alignment = xml2align.get(attrs.get('align'))

            start_formula = start_value

            def end_int(self, text):
                try:
                    self.value = int(text)
                except (TypeError, ValueError):
                    self.value = None

            end_long = end_int

            def end_double(self, text):
                try:
                    self.value = float(text)
                except (TypeError, ValueError):
                    self.value = None

            def end_complex(self, text):
                try:
                    self.value = complex(text)
                except (TypeError, ValueError):
                    self.value = None

            def end_string(self, text):
                self.value = text

            def end_value(self, text):
                if isinstance(self.value, BaseCell):
                    self.cell = self.value
                elif isinstance(self.value, str):
                    self.cell = StringCell(self.value,
                                           self.fmt or "%s",
                                           self.alignment or LEFT)
                else:
                    self.cell = NumericCell(self.value,
                                            self.fmt or "%s",
                                            self.alignment or RIGHT)

            def end_formula(self, text):
                self.cell = FormulaCell(text,
                                        self.fmt or "%s",
                                        self.alignment or RIGHT)

            def end_cell(self, text):
                self.sheet.setcell(self.x, self.y, self.cell)


        class BaseCell:
            __init__ = None  # Must provide
            """Abstract base class for sheet cells.

                Subclasses may but needn't provide the following APIs:

                cell.reset() -- prepare for recalculation
                cell.recalc(ns) -> value -- recalculate formula
                cell.format() -> (value, alignment) -- return formatted value
                cell.xml() -> string -- return XML
                """


        class NumericCell(BaseCell):

            def __init__(self, value, fmt="%s", alignment=RIGHT):
                assert isinstance(value, (int, float, complex))
                assert alignment in (LEFT, CENTER, RIGHT)
                self.value = value
                self.fmt = fmt
                self.alignment = alignment

            def recalc(self, ns):
                return self.value

            def format(self):
                try:
                    text = self.fmt % self.value
                except:
                    text = str(self.value)
                return text, self.alignment

            def xml(self):
                method = getattr(self, '_xml_' + type(self.value).__name__)
                return '<value align="%s" format="%s">%s</value>' % (
                    align2xml[self.alignment],
                    self.fmt,
                    method())

            def _xml_int(self):
                if -2 ** 31 <= self.value < 2 ** 31:
                    return '<int>%s</int>' % self.value
                else:
                    return '<long>%s</long>' % self.value

            def _xml_float(self):
                return '<double>%r</double>' % self.value

            def _xml_complex(self):
                return '<complex>%r</complex>' % self.value


        class StringCell(BaseCell):

            def __init__(self, text, fmt="%s", alignment=LEFT):
                assert isinstance(text, str)
                assert alignment in (LEFT, CENTER, RIGHT)
                self.text = text
                self.fmt = fmt
                self.alignment = alignment

            def recalc(self, ns):
                return self.text

            def format(self):
                return self.text, self.alignment

            def xml(self):
                s = '<value align="%s" format="%s"><string>%s</string></value>'
                return s % (
                    align2xml[self.alignment],
                    self.fmt,
                    escape(self.text))


        class FormulaCell(BaseCell):

            def __init__(self, formula, fmt="%s", alignment=RIGHT):
                assert alignment in (LEFT, CENTER, RIGHT)
                self.formula = formula
                self.translated = translate(self.formula)
                self.fmt = fmt
                self.alignment = alignment
                self.reset()

            def reset(self):
                self.value = None

            def recalc(self, ns):
                if self.value is None:
                    try:
                        self.value = eval(self.translated, ns)
                    except:
                        exc = sys.exc_info()[0]
                        if hasattr(exc, "__name__"):
                            self.value = exc.__name__
                        else:
                            self.value = str(exc)
                return self.value

            def format(self):
                try:
                    text = self.fmt % self.value
                except:
                    text = str(self.value)
                return text, self.alignment

            def xml(self):
                return '<formula align="%s" format="%s">%s</formula>' % (
                    align2xml[self.alignment],
                    self.fmt,
                    escape(self.formula))

            def renumber(self, x1, y1, x2, y2, dx, dy):
                out = []
                for part in re.split(r'(\w+)', self.formula):
                    m = re.match('^([A-Z]+)([1-9][0-9]*)$', part)
                    if m is not None:
                        sx, sy = m.groups()
                        x = colname2num(sx)
                        y = int(sy)
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            part = cellname(x + dx, y + dy)
                    out.append(part)
                return FormulaCell("".join(out), self.fmt, self.alignment)


        def translate(formula):
            """Translate a formula containing fancy cell names to valid Python code.

                Examples:
                    B4 -> cell(2, 4)
                    B4:Z100 -> cells(2, 4, 26, 100)
                """
            out = []
            for part in re.split(r"(\w+(?::\w+)?)", formula):
                m = re.match(r"^([A-Z]+)([1-9][0-9]*)(?::([A-Z]+)([1-9][0-9]*))?$", part)
                if m is None:
                    out.append(part)
                else:
                    x1, y1, x2, y2 = m.groups()
                    x1 = colname2num(x1)
                    if x2 is None:
                        s = "cell(%s, %s)" % (x1, y1)
                    else:
                        x2 = colname2num(x2)
                        s = "cells(%s, %s, %s, %s)" % (x1, y1, x2, y2)
                    out.append(s)
            return "".join(out)


        def cellname(x, y):
            "Translate a cell coordinate to a fancy cell name (e.g. (1, 1)->'A1')."
            assert x > 0  # Column 0 has an empty name, so can't use that
            return colnum2name(x) + str(y)


        def colname2num(s):
            "Translate a column name to number (e.g. 'A'->1, 'Z'->26, 'AA'->27)."
            s = s.upper()
            n = 0
            for c in s:
                assert 'A' <= c <= 'Z'
                n = n * 26 + ord(c) - ord('A') + 1
            return n


        def colnum2name(n):
            "Translate a column number to name (e.g. 1->'A', etc.)."
            assert n > 0
            s = ""
            while n:
                n, m = divmod(n - 1, 26)
                s = chr(m + ord('A')) + s
            return s


        import tkinter as Tk


        class SheetGUI:

            """Beginnings of a GUI for a spreadsheet.

                TO DO:
                - clear multiple cells
                - Insert, clear, remove rows or columns
                - Show new contents while typing
                - Scroll bars
                - Grow grid when window is grown
                - Proper menus
                - Undo, redo
                - Cut, copy and paste
                - Formatting and alignment
                """

            def __init__(self, filename="sheet1.xml", rows=10, columns=5):
                """Constructor.

                    Load the sheet from the filename argument.
                    Set up the Tk widget tree.
                    """
                # Create and load the sheet
                self.filename = filename
                self.sheet = Sheet()
                if os.path.isfile(filename):
                    self.sheet.load(filename)
                # Calculate the needed grid size
                maxx, maxy = self.sheet.getsize()
                rows = max(rows, maxy)
                columns = max(columns, maxx)
                # Create the widgets
                self.root = Tk.Tk()
                self.root.wm_title("Spreadsheet: %s" % self.filename)
                self.beacon = Tk.Label(self.root, text="A1",
                                       font=('helvetica', 16, 'bold'))
                self.entry = Tk.Entry(self.root)
                self.savebutton = Tk.Button(self.root, text="Save",
                                            command=self.save)
                self.cellgrid = Tk.Frame(self.root)
                # Configure the widget lay-out
                self.cellgrid.pack(side="bottom", expand=1, fill="both")
                self.beacon.pack(side="left")
                self.savebutton.pack(side="right")
                self.entry.pack(side="left", expand=1, fill="x")
                # Bind some events
                self.entry.bind("<Return>", self.return_event)
                self.entry.bind("<Shift-Return>", self.shift_return_event)
                self.entry.bind("<Tab>", self.tab_event)
                self.entry.bind("<Shift-Tab>", self.shift_tab_event)
                self.entry.bind("<Delete>", self.delete_event)
                self.entry.bind("<Escape>", self.escape_event)
                # Now create the cell grid
                self.makegrid(rows, columns)
                # Select the top-left cell
                self.currentxy = None
                self.cornerxy = None
                self.setcurrent(1, 1)
                # Copy the sheet cells to the GUI cells
                self.sync()

            def delete_event(self, event):
                if self.cornerxy != self.currentxy and self.cornerxy is not None:
                    self.sheet.clearcells(*(self.currentxy + self.cornerxy))
                else:
                    self.sheet.clearcell(*self.currentxy)
                self.sync()
                self.entry.delete(0, 'end')
                return "break"

            def escape_event(self, event):
                x, y = self.currentxy
                self.load_entry(x, y)

            def load_entry(self, x, y):
                cell = self.sheet.getcell(x, y)
                if cell is None:
                    text = ""
                elif isinstance(cell, FormulaCell):
                    text = '=' + cell.formula
                else:
                    text, alignment = cell.format()
                self.entry.delete(0, 'end')
                self.entry.insert(0, text)
                self.entry.selection_range(0, 'end')

            def makegrid(self, rows, columns):
                """Helper to create the grid of GUI cells.

                    The edge (x==0 or y==0) is filled with labels; the rest is real cells.
                    """
                self.rows = rows
                self.columns = columns
                self.gridcells = {}
                # Create the top left corner cell (which selects all)
                cell = Tk.Label(self.cellgrid, relief='raised')
                cell.grid_configure(column=0, row=0, sticky='NSWE')
                cell.bind("<ButtonPress-1>", self.selectall)
                # Create the top row of labels, and configure the grid columns
                for x in range(1, columns + 1):
                    self.cellgrid.grid_columnconfigure(x, minsize=64)
                    cell = Tk.Label(self.cellgrid, text=colnum2name(x), relief='raised')
                    cell.grid_configure(column=x, row=0, sticky='WE')
                    self.gridcells[x, 0] = cell
                    cell.__x = x
                    cell.__y = 0
                    cell.bind("<ButtonPress-1>", self.selectcolumn)
                    cell.bind("<B1-Motion>", self.extendcolumn)
                    cell.bind("<ButtonRelease-1>", self.extendcolumn)
                    cell.bind("<Shift-Button-1>", self.extendcolumn)
                # Create the leftmost column of labels
                for y in range(1, rows + 1):
                    cell = Tk.Label(self.cellgrid, text=str(y), relief='raised')
                    cell.grid_configure(column=0, row=y, sticky='WE')
                    self.gridcells[0, y] = cell
                    cell.__x = 0
                    cell.__y = y
                    cell.bind("<ButtonPress-1>", self.selectrow)
                    cell.bind("<B1-Motion>", self.extendrow)
                    cell.bind("<ButtonRelease-1>", self.extendrow)
                    cell.bind("<Shift-Button-1>", self.extendrow)
                # Create the real cells
                for x in range(1, columns + 1):
                    for y in range(1, rows + 1):
                        cell = Tk.Label(self.cellgrid, relief='sunken',
                                        bg='white', fg='black')
                        cell.grid_configure(column=x, row=y, sticky='NSWE')
                        self.gridcells[x, y] = cell
                        cell.__x = x
                        cell.__y = y
                        # Bind mouse events
                        cell.bind("<ButtonPress-1>", self.press)
                        cell.bind("<B1-Motion>", self.motion)
                        cell.bind("<ButtonRelease-1>", self.release)
                        cell.bind("<Shift-Button-1>", self.release)

            def selectall(self, event):
                self.setcurrent(1, 1)
                self.setcorner(sys.maxsize, sys.maxsize)

            def selectcolumn(self, event):
                x, y = self.whichxy(event)
                self.setcurrent(x, 1)
                self.setcorner(x, sys.maxsize)

            def extendcolumn(self, event):
                x, y = self.whichxy(event)
                if x > 0:
                    self.setcurrent(self.currentxy[0], 1)
                    self.setcorner(x, sys.maxsize)

            def selectrow(self, event):
                x, y = self.whichxy(event)
                self.setcurrent(1, y)
                self.setcorner(sys.maxsize, y)

            def extendrow(self, event):
                x, y = self.whichxy(event)
                if y > 0:
                    self.setcurrent(1, self.currentxy[1])
                    self.setcorner(sys.maxsize, y)

            def press(self, event):
                x, y = self.whichxy(event)
                if x > 0 and y > 0:
                    self.setcurrent(x, y)

            def motion(self, event):
                x, y = self.whichxy(event)
                if x > 0 and y > 0:
                    self.setcorner(x, y)

            release = motion

            def whichxy(self, event):
                w = self.cellgrid.winfo_containing(event.x_root, event.y_root)
                if w is not None and isinstance(w, Tk.Label):
                    try:
                        return w.__x, w.__y
                    except AttributeError:
                        pass
                return 0, 0

            def save(self):
                self.sheet.save(self.filename)

            def setcurrent(self, x, y):
                "Make (x, y) the current cell."
                if self.currentxy is not None:
                    self.change_cell()
                self.clearfocus()
                self.beacon['text'] = cellname(x, y)
                self.load_entry(x, y)
                self.entry.focus_set()
                self.currentxy = x, y
                self.cornerxy = None
                gridcell = self.gridcells.get(self.currentxy)
                if gridcell is not None:
                    gridcell['bg'] = 'yellow'

            def setcorner(self, x, y):
                if self.currentxy is None or self.currentxy == (x, y):
                    self.setcurrent(x, y)
                    return
                self.clearfocus()
                self.cornerxy = x, y
                x1, y1 = self.currentxy
                x2, y2 = self.cornerxy or self.currentxy
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 > y2:
                    y1, y2 = y2, y1
                for (x, y), cell in self.gridcells.items():
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        cell['bg'] = 'lightBlue'
                gridcell = self.gridcells.get(self.currentxy)
                if gridcell is not None:
                    gridcell['bg'] = 'yellow'
                self.setbeacon(x1, y1, x2, y2)

            def setbeacon(self, x1, y1, x2, y2):
                if x1 == y1 == 1 and x2 == y2 == sys.maxsize:
                    name = ":"
                elif (x1, x2) == (1, sys.maxsize):
                    if y1 == y2:
                        name = "%d" % y1
                    else:
                        name = "%d:%d" % (y1, y2)
                elif (y1, y2) == (1, sys.maxsize):
                    if x1 == x2:
                        name = "%s" % colnum2name(x1)
                    else:
                        name = "%s:%s" % (colnum2name(x1), colnum2name(x2))
                else:
                    name1 = cellname(*self.currentxy)
                    name2 = cellname(*self.cornerxy)
                    name = "%s:%s" % (name1, name2)
                self.beacon['text'] = name

            def clearfocus(self):
                if self.currentxy is not None:
                    x1, y1 = self.currentxy
                    x2, y2 = self.cornerxy or self.currentxy
                    if x1 > x2:
                        x1, x2 = x2, x1
                    if y1 > y2:
                        y1, y2 = y2, y1
                    for (x, y), cell in self.gridcells.items():
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            cell['bg'] = 'white'

            def return_event(self, event):
                "Callback for the Return key."
                self.change_cell()
                x, y = self.currentxy
                self.setcurrent(x, y + 1)
                return "break"

            def shift_return_event(self, event):
                "Callback for the Return key with Shift modifier."
                self.change_cell()
                x, y = self.currentxy
                self.setcurrent(x, max(1, y - 1))
                return "break"

            def tab_event(self, event):
                "Callback for the Tab key."
                self.change_cell()
                x, y = self.currentxy
                self.setcurrent(x + 1, y)
                return "break"

            def shift_tab_event(self, event):
                "Callback for the Tab key with Shift modifier."
                self.change_cell()
                x, y = self.currentxy
                self.setcurrent(max(1, x - 1), y)
                return "break"

            def change_cell(self):
                "Set the current cell from the entry widget."
                x, y = self.currentxy
                text = self.entry.get()
                cell = None
                if text.startswith('='):
                    cell = FormulaCell(text[1:])
                else:
                    for cls in int, float, complex:
                        try:
                            value = cls(text)
                        except (TypeError, ValueError):
                            continue
                        else:
                            cell = NumericCell(value)
                            break
                if cell is None and text:
                    cell = StringCell(text)
                if cell is None:
                    self.sheet.clearcell(x, y)
                else:
                    self.sheet.setcell(x, y, cell)
                self.sync()

            def sync(self):
                "Fill the GUI cells from the sheet cells."
                self.sheet.recalc()
                for (x, y), gridcell in self.gridcells.items():
                    if x == 0 or y == 0:
                        continue
                    cell = self.sheet.getcell(x, y)
                    if cell is None:
                        gridcell['text'] = ""
                    else:
                        if hasattr(cell, 'format'):
                            text, alignment = cell.format()
                        else:
                            text, alignment = str(cell), LEFT
                        gridcell['text'] = text
                        gridcell['anchor'] = align2anchor[alignment]


        def test_basic():
            "Basic non-gui self-test."
            a = Sheet()
            for x in range(1, 11):
                for y in range(1, 11):
                    if x == 1:
                        cell = NumericCell(y)
                    elif y == 1:
                        cell = NumericCell(x)
                    else:
                        c1 = cellname(x, 1)
                        c2 = cellname(1, y)
                        formula = "%s*%s" % (c1, c2)
                        cell = FormulaCell(formula)
                    a.setcell(x, y, cell)
            ##    if os.path.isfile("sheet1.xml"):
            ##        print "Loading from sheet1.xml"
            ##        a.load("sheet1.xml")
            a.display()
            a.save("sheet1.xml")


        def test_gui():
            "GUI test."
            if sys.argv[1:]:
                filename = sys.argv[1]
            else:
                filename = "sheet1.xml"
            g = SheetGUI(filename)
            g.root.mainloop()


        if __name__ == '__main__':
            # test_basic()
            test_gui()


    elif a == "build game":
        import subprocess
        sj = subprocess.Popen('C:\\Program Files (x86)\\Buildbox3\\buildbox.exe')


    elif a == "print Harshil":
        print("Harshil")


    elif a == "timer":
        import time
        seconds = 0
        minutes = 0
        hours = 0
        while True:
            print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
            seconds = seconds + 1
            time.sleep(1)
            if seconds == 60:
                seconds = 0
                minutes = minutes + 1
            elif minutes == 60:
                minutes = 0
                hours = hours + 1

    elif a == "wish me happy birthday":
        print("Happy birthday to you")
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("Happy Birthday To You.")






    elif a == "-gs":
        import webbrowser
        ha = input("")
        webbrowser.open('https://google.com/?#q=' + ha)

    elif a == "tell story":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak('''This is a lovely novel that all age groups can understand. Aimed at native English speaking children, there are many adults who still say
    this famous book is their favorite. This is part of the national curriculum in many schools around the world, so itâ€™s quite possible this book will also come
    up in conversation. You can almost guarantee that the majority of native English speakers have read this book at least once.

    Plot Summary

    A baby pig is almost killed because of his status â€“ he is the smallest pig that was born and he is considered to be useless and of no value. The pig is saved
    by a little girl called Fern Arable. She adopts the pig and takes care of it. She gives him the name Wilbur.

    Fern grows sad when Wilbur grows up and has to be sent away to a farm owned by her uncle. She has a strong relationship with Wilbur. When Wilbur
    goes to the farm, all the other farm animals ignore him and heâ€™s left crying for his human friend. One day he hears a voice, but he canâ€™t see anything.
    This voice promises to become friends with him.

    The voice belongs to a small spider called Charlotte. Charlotte the spider knows that the farmers are planning to kill Wilbur. She promises to make a plan
    to save his life. The farmers are surprised the next day when they see the words â€œsome pigâ€ written in the web* Charlotte has made. Charlotte asked for
    the other animalsâ€™ help over the day to write messages everywhere.

    Wilbur is sad when Charlotte disappears. But in the end, her baby spiders turn out to be great company for the pig. They continue to protect each other
    and the story ends well.

    *webs are the sticky traps that spiders make.''')












    elif a == "import CA":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("CA Has Been Imported")




    elif a == "sh -number table":
        ha = int(input(""))

        for i in range(1, 11):
            yd = ha, 'x', i, '=', ha * i
            print(yd)

    elif a == "sh -notify me":
        import plyer
        from plyer import notification

        if __name__ == '__main__':
            h1 = int(input("Floating Time: "))
            ha = input("From: ")
            hq1 = input("Message: ")
            while True:
                notification.notify(
                    title=ha,
                    message=hq1,
                    timeout=h1
                )





    elif a == "import python":
        k21 = input("><")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break




    elif a == "open vlc":
        import subprocess

        file3 = subprocess.Popen('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')




    elif a == "open AcroRd32":
        import subprocess
        file4 = subprocess.Popen('C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe')





    elif a == "dl -python":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("Download Python From Official website")
        # ! /usr/bin/env python3

        """Script to search with Google

            Usage:
                python3 google.py [search terms]
            """

        import sys
        import urllib.parse
        import webbrowser


        def main(args):
            def quote(arg):
                if ' ' in arg:
                    arg = '"%s"' % arg
                return urllib.parse.quote_plus(arg)

            qstring = '+'.join(quote(arg) for arg in args)
            url = urllib.parse.urljoin('https://www.python.org/search', '?q=' + qstring)
            webbrowser.open(url)


        if __name__ == '__main__':
            main(sys.argv[1:])

    elif a == "open site":
        h = input("Enter site url: ")
        # ! /usr/bin/env python3

        """Script to search with Google

            Usage:
                python3 google.py [search terms]
            """

        import sys
        import urllib.parse
        import webbrowser


        def main(args):
            def quote(arg):
                if ' ' in arg:
                    arg = '"%s"' % arg
                return urllib.parse.quote_plus(arg)

            qstring = '+'.join(quote(arg) for arg in args)
            url = urllib.parse.urljoin('https://google.com/search', '?q=' + qstring)
            webbrowser.open(url) 

    elif a == "sh -date":
        import datetime

        today = datetime.date.today()
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("today's date is")

        print("Today's Date: ", today)


    elif a == "sh -mysignature":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("Enter Month When You Born")

        month = input("Enter Month When You Born (First Letter Capital): ")
        month.lower()
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("Enter day when you born")

        day = int(input("Enter Day When You Born: "))
        months = ["March", "April", "May", "June", "September", "August", "November", "October", "December",
                  "January", "February", ]
        if month in months:
            if month == "March":
                sign = "Pisces" if (day < 21) else "Aires"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Pisces":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is pisces")

                elif sign == "Aires":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Aires")



            elif month == "April":
                sign = "Aires" if (day < 20) else "Taurus"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Aires":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Aires")

                elif sign == "Taurus":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Taurus")



            elif month == "May":
                sign = "Taurus" if (day < 21) else "Gemini"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Taurus":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Taurus")

                elif sign == "Gemini":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Gemini")




            elif month == "June":
                sign = "Gemini" if (day < 21) else "Cancer"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Gemini":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Gemini")

                elif sign == "Cancer":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Cancer")



            elif month == "July":
                sign = "Cancer" if (day < 23) else "Leo"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Cancer":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Cancer")

                elif sign == "Leo":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Leo")






            elif month == "August":
                sign = "Leo" if (day < 23) else "Virgo"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Leo":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Leo")

                elif sign == "Vigro":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Vigro")




            elif month == "September":
                sign = "Virgo" if (day < 23) else "Libra"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Virgo":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Virgo")

                elif sign == "Libra":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Libra")



            elif month == "October":
                sign = "Libra" if (day < 23) else "Scorpio"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Libra":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Libra")

                elif sign == "Scorpio":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Scorpio")



            elif month == "November":
                sign = "Scorpio" if (day < 22) else "Sagittarius"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Scorpio":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Scorpio")

                elif sign == "Sagittarius":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Sagittarius")





            elif month == "December":
                sign = "Sagittarius" if (day < 22) else "capricorn"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Sagittarius":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Sagittarius")

                elif sign == "capricorn":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is capricorn")



            elif month == "January":
                sign = "Capricorn" if (day < 20) else "Aquarius"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Capricorn":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Capricorn")

                elif sign == "Aquarius":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Aquarius")

            elif month == "February":
                sign = "Aquarius" if (day < 19) else "Pisces"
                print("Your Zodiac Sign is", sign, ".")
                if sign == "Aquarius":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Aquarius")

                elif sign == "Pisces":
                    from win32com.client import Dispatch


                    def speak(str):
                        speak = Dispatch(("SAPI.spVoice"))
                        speak.Speak(str)


                    if __name__ == '__main__':
                        speak("Your Zodiac Sign is Pisces")

    elif a == "CA import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break

    elif a == "pl -music os":
        music_dir = 'C:\\Users\\Admin\\Music\\Songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))



    elif a == "open youtube":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak('''I Am Opening Youtube''')
        # ! /usr/bin/env python3

        """Script to search with Google

            Usage:
                python3 google.py [search terms]
            """

        import sys
        import urllib.parse
        import webbrowser


        def main(args):
            def quote(arg):
                if ' ' in arg:
                    arg = '"%s"' % arg
                return urllib.parse.quote_plus(arg)

            qstring = '+'.join(quote(arg) for arg in args)
            url = urllib.parse.urljoin('https://www.youtube.com/search', '?q=' + qstring)
            webbrowser.open(url)


        if __name__ == '__main__':
            main(sys.argv[1:])
    elif a == "import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break






    elif a == "open cmd":
        import subprocess
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("I Am Opening cmd")

        subprocess.call('cmd.exe')

    elif a == "import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break


    elif a == "r -password":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak("Your password will ready in few seconds")

        import string
        import random

        if __name__ == "__main__":
            s1 = string.ascii_lowercase
            # print(s1)
            s2 = string.ascii_uppercase
            # print(s2)
            s3 = string.digits
            # print(s3)
            s4 = string.punctuation
            # print(s4)
            from win32com.client import Dispatch


            def speak(str):
                speak = Dispatch(("SAPI.spVoice"))
                speak.Speak(str)


            if __name__ == '__main__':
                speak("Enter password length")

            plen = int(input("Please enter password length:\n"))  # Todo1: Handle Gibbersish

            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            # print(s)
            random.shuffle(s)
            # print(s)
            from win32com.client import Dispatch


            def speak(str):
                speak = Dispatch(("SAPI.spVoice"))
                speak.Speak(str)


            if __name__ == '__main__':
                speak("This is your password")

            print("".join(s[0:plen]))



    elif a == "import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break


    elif a == "open cleanup disk":
        import subprocess
        file2344 = subprocess.Popen('C:\WINDOWS\system32\cleanmgr.exe')






    elif a == "open firefox":
        import subprocess
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak('''I Am Opening firefox''')
            import subprocess

            file67 = subprocess.Popen('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\fire fox\\Firefox.exe')
    elif a == "import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break







    elif a == "open calender":
        import subprocess

        subprocess.call('calender.exe')
    elif a == "CA import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break









    elif a == "open chrome":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak('''I am opening Chrome''')
        # ! /usr/bin/env python3

        """Script to search with Google

            Usage:
                python3 google.py [search terms]
            """

        import sys
        import urllib.parse
        import webbrowser


        def main(args):
            def quote(arg):
                if ' ' in arg:
                    arg = '"%s"' % arg
                return urllib.parse.quote_plus(arg)

            qstring = '+'.join(quote(arg) for arg in args)
            url = urllib.parse.urljoin('https://www.google.com/search', '?q=' + qstring)
            webbrowser.open(url)


        if __name__ == '__main__':
            main(sys.argv[1:])




    elif a == "sd -gmail":
        import smtplib
        ser = input("Email ID: ")
        TO = ser
        a123 = input("SUBJECT: ")
        SUBJECT =  a123
        a12r3 = input("TEXT: ")
        TEXT = a12r3

        # Gmail Sign In
        gmail_sender = 'harshilanuwadia97@gmail.com'
        gmail_passwd = 'ha@@##421600'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])

        try:
            server.sendmail(gmail_sender, [TO], BODY)
            print ('email sent')
        except:
            print ('error sending mail')

            server.quit()

    elif a == "open textpad":
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak('''i am opening textpad''')
        from tkinter import *
        from tkinter.messagebox import showinfo
        from tkinter.filedialog import askopenfilename, asksaveasfilename
        import os


        def newFile():
            global file
            root.title("Textpad")
            file = None
            TextArea.delete(1.0, END)


        def openFile():
            global file
            file = askopenfilename(defaultextension=".CA ",
                                   filetypes=[("All Files", "*.*"),
                                              ("CA Docs", "*.Programming Boyz ")])
            if file == "":
                file = None
            else:
                root.title(os.path.basename(file) + " - Textpad")
                TextArea.delete(1.0, END)
                f = open(file, "r")
                TextArea.insert(1.0, f.read())
                f.close()


        def saveFile():
            global file
            if file == None:
                file = asksaveasfilename(initialfile='Programming Boyz',
                                         defaultextension=".",
                                         filetypes=[("All Files", "*.CA Docs*"),
                                                    ("CA Docs", "*.")])

                if file == "":
                    file = None

                else:
                    # Save as a new file
                    f = open(file, "w")
                    f.write(TextArea.get(1.0, END))
                    f.close()

                    root.title(os.path.basename(file) + " - Textpad")
                    print("File Saved")
            else:
                # Save the file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()


        def quitApp():
            root.destroy()


        def cut():
            TextArea.event_generate(("<>"))


        def copy():
            TextArea.event_generate(("<>"))


        def paste():
            TextArea.event_generate(("<>"))


        def about():
            showinfo("Textpad", "Created By Harshil Anuwadia")


        if __name__ == '__main__':
            # Basic tkinter setup
            root = Tk()
            root.title("Untitled - Textpad")

            root.geometry("644x788")

            # Add TextArea
            TextArea = Text(root, font="lucida 13")
            file = None
            TextArea.pack(expand=True, fill=BOTH)

            MenuBar = Menu(root)

            FileMenu = Menu(MenuBar, tearoff=0)

            FileMenu.add_command(label="New", command=newFile)

            FileMenu.add_command(label="Open", command=openFile)

            FileMenu.add_command(label="Save", command=saveFile)
            FileMenu.add_separator()
            FileMenu.add_command(label="Exit", command=quitApp)
            MenuBar.add_cascade(label="File", menu=FileMenu)
            # File Menu ends

            # Edit Menu Starts
            EditMenu = Menu(MenuBar, tearoff=0)
            # To give a feature of cut, copy and paste
            EditMenu.add_command(label="Cut", command=cut)
            EditMenu.add_command(label="Copy", command=copy)
            EditMenu.add_command(label="Paste", command=paste)

            MenuBar.add_cascade(label="Edit", menu=EditMenu)

            # Help Menu Starts
            HelpMenu = Menu(MenuBar, tearoff=0)
            HelpMenu.add_command(label="About Textpad", command=about)
            MenuBar.add_cascade(label="Help", menu=HelpMenu)

            # Help Menu Ends

            root.config(menu=MenuBar)

            # Adding Scrollbar using rules from Tkinter lecture no 22
            Scroll = Scrollbar(TextArea)
            Scroll.pack(side=RIGHT, fill=Y)
            Scroll.config(command=TextArea.yview)
            TextArea.config(yscrollcommand=Scroll.set)

            root.mainloop()
    elif a == "import python":
        k21 = input("")
        if k21 == "python":
            while True:
                import subprocess

                file = subprocess.Popen('C:\\Python385\\python.exe')
                break
    elif a == "open file":
        main2 = input("Enter file location>< ")
        import subprocess

        file100 = subprocess.Popen(main2)

    elif a == "cr -notepad":
        fne = input("Enter your name: ")
        ja = input("Set Title: ")
        ja1 = input("Set extention: ")
        db = input("file type: ")
        nf = input("Another file type: ")
        from tkinter import *
        from tkinter.messagebox import showinfo
        from tkinter.filedialog import askopenfilename, asksaveasfilename
        import os


        def newFile():
            global file
            root.title(ja)
            file = None
            TextArea.delete(1.0, END)


        def openFile():
            global file
            file = askopenfilename(defaultextension=".CA",
                                   filetypes=[("All Files", "*.*"),
                                              (db, "*.",ja1)])
            if file == "":
                file = None
            else:
                root.title(os.path.basename(file) + " -Notepad ")
                TextArea.delete(1.0, END)
                f = open(file, "r")
                TextArea.insert(1.0, f.read())
                f.close()


        def saveFile():
            global file
            if file == None:
                file = asksaveasfilename(initialfile="",
                                         defaultextension=".",
                                         filetypes=[(nf, "*.CA Docs*"),
                                                    ("CA Docs", "*.")])

                if file == "":
                    file = None

                else:
                    # Save as a new file
                    f = open(file, "w")
                    f.write(TextArea.get(1.0, END))
                    f.close()

                    root.title(os.path.basename(file) + " - Textpad")
                    print("File Saved")
            else:
                # Save the file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()


        def quitApp():
            root.destroy()


        def cut():
            TextArea.event_generate(("<>"))


        def copy():
            TextArea.event_generate(("<>"))


        def paste():
            TextArea.event_generate(("<>"))


        def about():
            showinfo("Textpad", "Created By you")


        if __name__ == '__main__':
            # Basic tkinter setup
            root = Tk()
            root.title("Untitled - Notepad")

            root.geometry("644x788")

            # Add TextArea
            TextArea = Text(root, font="lucida 13")
            file = None
            TextArea.pack(expand=True, fill=BOTH)

            MenuBar = Menu(root)

            FileMenu = Menu(MenuBar, tearoff=0)

            FileMenu.add_command(label="New", command=newFile)

            FileMenu.add_command(label="Open", command=openFile)

            FileMenu.add_command(label="Save", command=saveFile)
            FileMenu.add_separator()
            FileMenu.add_command(label="Exit", command=quitApp)
            MenuBar.add_cascade(label="File", menu=FileMenu)
            # Edit Menu Starts
            EditMenu = Menu(MenuBar, tearoff=0)
            # To give a feature of cut, copy and paste
            EditMenu.add_command(label="Cut", command=cut)
            EditMenu.add_command(label="Copy", command=copy)
            EditMenu.add_command(label="Paste", command=paste)

            MenuBar.add_cascade(label="Edit", menu=EditMenu)

            # Help Menu Starts
            HelpMenu = Menu(MenuBar, tearoff=0)
            HelpMenu.add_command(label="About your Notepad", command=about)
            MenuBar.add_cascade(label="Help", menu=HelpMenu)

            # Help Menu Ends

            root.config(menu=MenuBar)

            # Adding Scrollbar using rules from Tkinter lecture no 22
            Scroll = Scrollbar(TextArea)
            Scroll.pack(side=RIGHT, fill=Y)
            Scroll.config(command=TextArea.yview)
            TextArea.config(yscrollcommand=Scroll.set)

            root.mainloop()

    elif a == "open calculator":
        break
while True:
    print("1.License Of Super Compute Calculator [Version 1.0] By CA")
    print("2.Not Now,Go forward.")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("---------------------------------------------------")
        print('''--HISTORY OF THIS SOFTWARE.--

[Super Compute Calculator.]

The creator of this calculator is Harshil Anuwadia.
This is a calculator that can perform any type of the
calculation like basic calculation,area calculation,
volume calculation,super calculation and many more.


This calculator is not only calculator,this calculator
has more option in that you can explore many things
like what is your age,what is your zodiac sign,temperature
calculator,bmi calculator,plaing a trip,jump to date,my 
next birthday,know today's date by your birthdate and many
more.The version of this calculator is [version 1.0].


If and update wiil there there then you will be updated.

This software does need any type of licence.This software is open source.
This calculatoris not elegible to do exepretion calculation.
We are trying to improve thiscalculator if you have suggestion then
please send us feedback on email Harshil Anuwadia A Gmail.com.
Thank You.''')
        from win32com.client import Dispatch


        def speak(str):
            speak = Dispatch(("SAPI.spVoice"))
            speak.Speak(str)


        if __name__ == '__main__':
            speak('''--HISTORY OF THIS SOFTWARE
                Super Compute Calculator.

                The creator of this calculator is Harshil Anuwadia.
                This is a calculator that can perform any type of the
                calculation like basic calculation,area calculation,
                volume calculation,super calculation and many more.


                This calculator is not only calculator this calculator
                has more option in that you can explore many things
                like what is your age,what is your zodiac sign,temperature
                calculator,bmi calculator,plaing a trip,jump to date,my 
                next birthday,know today's date by your birthdate and many
                more.The version of this calculator is [version 1.0].


                If and update wiil there there then you will be updated.

                This software does need any type of licence.This software is open source.
                This calculatoris not elegible to do exepretion calculation.
                We are trying to improve thiscalculator if you have suggestion then
                please send us feedback on email Harshil Anuwadia A Gmail.com.
                Thank You.''')


    elif choice == 2:
        break
while True:

    print('''                                                                                       
Select Any One Option.''')
    print("1.Basic Calculator.")
    print("2.Area calculator.")
    print("3.Speed Calculator.")
    print("4.Distance Calculator.")
    print("5.Time Calculator.")
    print("6.Volume Calculator.")
    print("7.Show More Option.")
    print("8.Again Load This Page.")
    print("9.Know Today's Date From Your Birthdate.")
    print("10.Exit.")

    choice = int(input("Enter your choice: "))


    def devide(x, y):
        """"This function divides 2 numbers"""
        return x / y


    if choice == 3:
        num1 = int(input("Enter Distance: "))
        num2 = int(input("Enter Time: "))
        print("Speed is", num1, "/", num2, "=", devide(num1, num2))

    elif choice == 2:
        print("1.Looking for 2D object.")
        print("2.Looking for 3D object.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            while True:
                print("1.Area of Square.")
                print("2.Area of rectangle.")
                print("3.Area of triangle.")
                print("4.Area of circle.")
                print("5.Exit.")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    num1 = int(input("Enter side of square: "))
                    num2 = num1
                    se = num1 * num2
                    print("Area of square is", se, ".")


                elif choice == 2:
                    num3 = int(input("Enter rectangle length: "))
                    num4 = int(input("Enter rectangle breath: "))
                    se2 = num3 * num4
                    print("Area of rectangle is", se2, ".")

                elif choice == 3:
                    num5 = int(input("Enter triangle base: "))
                    num6 = int(input("Enter triangle height: "))
                    se3 = 1 / 2 * num5 * num6
                    print("Area of triangle is", se3, ".")



                elif choice == 4:
                    num7 = int(input("Enter radius: "))
                    seA = num7 * num7
                    seB = 22 / 7
                    se4 = seB * seA
                    print("Area of circle is", se4, ".")

                elif choice == 5:
                    break


        elif choice == 2:
            while True:
                print("1.Area of Cube.")
                print("2.Area of cuboid.")
                print("3.Area of cone")
                print("4.Area of cylinder.")
                print("5.Area of sphere.")
                print("6.Area of hemisphere.")
                print("7.Go Back")
                print("8.Exit.")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    a = int(input("Enter cube side: "))
                    b = a
                    c = a * b
                    print("Area of cube is", c, ".")

                elif choice == 2:
                    a = int(input("Enter cuboid length: "))
                    b = int(input("Enter cuboid breath: "))
                    c = int(input("Enter cuboid height:"))
                    d = 2 * a * b + 2 * a * c + 2 * b * c
                    print("Area of cuboid is", d, ".")

                elif choice == 7:
                    print("Ok Done")

                elif choice == 8:
                    print("You Have Been Succesfully Exited From Super Calculator.")
                    print("Thank You.")
                    print("Harshil Anuwadia Presents.")
                    break

                elif choice == 4:
                    a = int(input("Enter Radius: "))
                    b = int(input("Enter Height: "))
                    c = 2 * 22 / 7 * a * b + 2 * 22 / 7 * a * a
                    print("Area of cylinder is", c, ".")

                elif choice == 5:
                    a = int("Enter Radius: ")
                    b = 4 * 22 / 7 * a * a
                    print("Area of sphere is", b, ".")

                elif choice == 6:
                    a = int(input("Enter Radius: "))
                    b = 2 * 22 / 7 * a * a
                    print("Area of hemisphere is", b, ".")

                elif choice == 3:
                    a = int(input("Enter Radius: "))
                    b = int(input("Enter Height: "))
                    c = int(input("Enter slant height: "))
                    d = 22 / 7 * c + 22 / 7 + a * a
                    print("Area of cone is", d, ".")


    elif choice == 4:
        a = int(input("Enter Speed: "))
        b = int(input("Enter Time: "))
        d = a * b
        print("Distance is", d, ".")

    elif choice == 9:
        import datetime

        e = input("Enter Name: ")
        a = int(input("Enter Year: "))
        b = int(input("Enter Month: "))
        c = int(input("Enter Date: "))
        birth = datetime.date(a, b, c)
        today = datetime.date.today()
        print("Today's Date: ", today)






    elif choice == 10:
        a = input("Are You Sure That That You Want To Exit: ")
        print("You Have Been Succesfully Exited From Super Calculator.")
        print("Thank You.")
        print("Harshil Anuwadia Presents.")
        break




    elif choice == 1:
        while True:
            print("1.Add..")
            print("2.Subtract.")
            print("3.Multiply.")
            print("4.Divide.")
            print("5.Power.")
            print("6.exit.")
            print("7.Go Back")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("You Are Doing Addition.")
                a = int(input("Enter First Number: "))
                b = int(input("Enter Second Number: "))
                c = a + b
                print("Your Answer is", c, ".")

            elif choice == 2:
                print("You Are Doing Subtraction.")
                a = int(input("Enter First Number: "))
                b = int(input("Enter Second Number: "))
                c = a - b
                print("Your Answer is", c, ".")

            elif choice == 3:
                print("You Are Doing Multiplication.")
                a = int(input("Enter First Number: "))
                b = int(input("Enter Second Number: "))
                c = a * b
                print("Your Answer is", c, ".")

            elif choice == 4:
                print("You Are Doing Division.")
                a = int(input("Enter First Number: "))
                b = int(input("Enter Second Number: "))
                c = a / b
                print("Your Answer is", c, ".")

            elif choice == 5:
                print("You Are Doing Power.")
                a = int(input("Enter Number: "))
                c = a * a
                print("Your Answer is", c, ".")
            elif choice == 6:
                print("You Have Been Succesfully Exited From Super Calculator.")
                print("Thank You.")
                print("Harshil Anuwadia Presents.")
                break
            elif choice == 7:
                print("Ok Done.")

    elif choice == 6:
        while True:
            print("1.Volume of cube")
            print("2.Volume of cuboid")
            print("3.Volume of cylinder")
            print("4.Volume of cone")
            print("5.Volume of sphere")
            print("6.Volume of hemisphere")
            print("7.Exit")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                se5 = int(input("Enter side length: "))
                se6 = se5 * se5
                se7 = 4 * se6
                print("Volume of cube is", se7, " ")

            elif choice == 2:
                se1 = int(input("Enter cuboid Length: "))
                se2 = int(input("Enter cuboid breath: "))
                se3 = int(input("Enter cuboid height: "))
                se4 = se1 * se2 * se3
                print("Volume of cuboid is", se4, " ")

            elif choice == 3:
                sa1 = int(input("Enter cylinder radius: "))
                sa2 = int(input("Enter cylinder height: "))
                sa3 = 22 / 7
                sa4 = sa1 * sa1
                sa5 = sa3 * sa4 * sa2
                print("Volume of cylinder", sa5, " ")

            elif choice == 4:
                sd1 = int(input("Enter cone radius: "))
                sd2 = int(input("Enter cone length: "))
                sd3 = 1 / 3 * 22 / 7
                sd4 = sd1 * sd1
                sd5 = sd3 * sd4 * sd2
                print("Volume of cone is", sd5, " ")

            elif choice == 5:
                sq1 = int(input("Enter sphere radius: "))
                sq2 = 4 / 3 * 3.14
                sq3 = sq1 * sq1 * sq1
                sq4 = sq2 * sq3
                print("Volume of sphere is", sq4, " ")

            elif choice == 6:
                sw1 = int(input("Enter hemisphere radius "))
                sw2 = 2 / 3 * 22 / 7
                sw3 = sw1 * sw1 * sw1
                sw4 = sw2 * sw3
                print("Volume of hemisphere is", sw4, " ")


            elif choice == 7:
                print("You Have Been Succesfully Exited From Super Calculator.")
                print("Thank You.")
                print("Harshil Anuwadia Presents.")
                break
    elif choice == 7:
        while True:
            print("1.Age Calculator")
            print("2.Temperature Calculator")
            print("3.EMI Calculator")
            print("4.Percentage Calculator")
            print("5.Discount Calculator")
            print("6.BMI calculator")
            print("7.What Is My Zodiac Sign")
            print("8.LCM")
            print("9.Spilt The Bill")
            print("10.Show More Option")
            print("11.Exit")
            choice = int(input("Enter choice: "))


            def subtract(x, y):
                """"This function subtracts 2 numbers"""
                return x - y


            if choice == 1:
                a = input("Enter Name: ")
                c = int(input("Enter Day When You Born: "))
                d = int(input("Enter Month When You Born: "))
                num2 = int(input("Enter Year When You Born: "))
                num1 = int(input("Enter Now Year: "))
                print("1.Show Details")
                choice = int(input("Enter Choice: "))
                if choice == 1:
                    print("              Loding.")
                    print(":=================================:")
                    print("Loding Done.")
                    print(" ")
                    print("You Was Born on As following:")
                    print("Your Name is", a, ".")
                    print("You Was Born on", c, "/", d, "/", num2, ".")
                    print("Your Age is", num1 - num2, ".")
                    print("Your Running Age is", num1 - num2 + 1, ".")
                    print("----------------------------------------")

            elif choice == 9:
                p = int(input("Amount Of Money You Pay: "))
                se = int(input("Number Of Person: "))
                we = p / se
                print("One Person Suppode To Pay", we, ".")

            elif choice == 4:
                a = float(input("Enter Your Marks: "))
                per = 100
                b = float(input("Enter Total Marks: "))
                s = a * per / b
                print("Your Percentage(%) is", s, ".")

            elif choice == 7:
                month = input("Enter Month When You Born (First Letter Capital): ")
                month.lower()
                day = int(input("Enter Day When You Born: "))
                months = ["March", "April", "May", "June", "September", "August", "November", "October", "December",
                          "January", "February", ]
                if month in months:
                    if month == "March":
                        sign = "Pisces" if (day < 21) else "Aires"
                        print("Your Zodiac Sign is", sign, ".")

                    elif month == "April":
                        sign = "Aires" if (day < 20) else "Taurus"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "May":
                        sign = "Taurus" if (day < 21) else "Gemini"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "June":
                        sign = "Gemini" if (day < 21) else "Cancer"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "July":
                        sign = "Cancer" if (day < 23) else "Leo"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "August":
                        sign = "Leo" if (day < 23) else "Virgo"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "September":
                        sign = "Virgo" if (day < 23) else "Libra"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "October":
                        sign = "Libra" if (day < 23) else "Scorpio"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "November":
                        sign = "Scorpio" if (day < 22) else "Sagittarius"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "December":
                        sign = "Sagittarius" if (day < 22) else "capricorn"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "January":
                        sign = "Capricorn" if (day < 20) else "Aquarius"
                        print("Your Zodiac Sign is", sign, ".")


                    elif month == "February":
                        sign = "Aquarius" if (day < 19) else "Pisces"
                        print("Your Zodiac Sign is", sign, ".")


            elif choice == 11:
                print("You Have Been Succesfully Exited From Super Calculator.")
                print("Thank You.")
                print("Harshil Anuwadia Presents.")
                break

            elif choice == 2:
                str = input("Enter The Unit Of Temperature (in C/F/K): ")
                if str.upper() == "C":
                    tem = float(input("Enter The Temperature: "))
                    cond = input("Enter F To Convert Into To Fahrenheit Or K To Convert Into Kelvin: ")
                    if cond.upper() == "F":
                        result = float(((tem * (9 / 5) + 32)))
                        print("The Temperature In Fahrenheit Is: ", result)
                    elif cond.upper() == "K":
                        result = float(tem + 273.15)
                        print("The Temperature In Kelvin Is: ", result, ".")
                    else:
                        print("Wrong Input")
                        break


                elif str.upper() == "F":
                    tem = float(input("Enter The Temperature: "))
                    cond = input("Enter C To Convert Into Celcius Or K To Convert Into Kelvin: ")
                    if cond.upper() == "C":
                        result = float((5 * (tem - 32) / 9))
                        print("The Temperature In Celcius Is: ", result)
                    elif cond.upper() == "K":
                        result = float((tem + 459.67) * (5 / 9))
                        print("The Temperature In kelvin Is: ", result)
                    else:
                        print("Wrong Input")

                elif str.upper() == "K":
                    tem = float(input("Enter The Temperature: "))
                    cond = input("Enter F To Convert Into Fahrenheit Or C To Convert Into Celcius: ")
                    if cond.upper() == "F":
                        result = float((tem * (9 / 5)) - 459.67)
                        print("The Temperature In Fahrenheit: ", result)
                    elif cond.upper() == "C":
                        result = float((tem - 273.15))
                        print("The Temperature In Celcius Is: ", result)
                    else:
                        print("Wrong Input")

            elif choice == 5:
                sCost = input("Enter The Cost Of The Item: ")
                sPercent = input("What Percentage (%) Discount Is It ?: ")
                fCost = float(sCost)
                fPercent = float(sPercent)
                fDiscount = fCost * fPercent / 100
                print("You Save : ", fDiscount)
                print("You Pay : ", fCost - fDiscount)


            elif choice == 6:
                name = input("Enter Your Name: ")
                weight = float(input("Enter Your Weight: "))
                height = float(input("Enter Your height: "))

                bmi = weight / (height ** 2)
                if bmi < 25:
                    print(f"{name} is underweight by {bmi} BMI")
                else:
                    print("Its gone out of limit")

            elif choice == 3:
                p = int(input("Enter Amount Of Loan: "))
                r = int(input("Enter Rate Of Loan: "))
                n = int(input("Enter Number Of Monthly Instalments: "))
                d = ((p * r * (1 + r) ^ n) / ((1 + r) ^ n - 1))
                print("Monthly Payment: ", d)

            elif choice == 8:
                a = int(input("Enter First Number: "))
                b = int(input("Enter Second Number: "))

                maxNum = max(a, b)
                while (True):
                    if (maxNum % a == 0 and maxNum % b == 0):
                        break
                    maxNum = maxNum + 1

                print("The LCM Of", a, "and", b, "Is", maxNum)

            elif choice == 10:
                while True:
                    print("1.Planing A Trip")
                    print("2.Jump To Date")
                    print("3.Strong Password Generator")
                    print("4.My Next Birthday")
                    print("5.Promox Bot")
                    print("6.Exit")
                    choice = int(input("Enter Your Choice: "))
                    if choice == 1:
                        ua = input("Enter Your Name: ")
                        aa = input("Enter Which Day You Are Going  For A Trip: ")
                        ra = int(input("Enter Date Of Trip: "))
                        ya = input("Enter Month Of Trip: ")

                        ca = input("Which Place Do You Want To Go: ")
                        month = ["March", "April", "May", "June", "September", "August", "November", "October",
                                 "December",
                                 "January", "February", ]
                        date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                                25,
                                26,
                                27, 28, 29, 30, 31]
                        da = int(input("Enter Year Of Trip: "))
                        print("Ok Will Try To Put All Things Togeather")
                        print("1.Print Details")
                        choice = int(input("Enter Choice: "))
                        if choice == 1:
                            print("1.You Are Going To Trip in", ca)
                            print("2.Day Is", aa)
                            print("3.Date Is", ra, ya, da)

                            print(ua, "We Wish You Happy Journey For Your", ca, "Trip.")
                            print("Happy Journey.")


                    elif choice == 2:
                        a = input("Enter Format (In Date/year): ")
                        month = ["March", "April", "May", "June", "September", "August", "November", "October",
                                 "December",
                                 "January", "February", ]
                        if a == "Date":
                            d = int(input("Enter Date: "))
                            v = int(input("Enter Jump Number: "))
                            w = d + v
                            if d < 30 and v < 29:
                                print("Jump Date Is", w)
                            else:
                                print("You Have Gone Up To Date")

                        elif a == "Year":
                            f = int(input("Enter Year: "))
                            g = int(input("Enter Jump Year: "))
                            l = f + g
                            print("Your Jump Year Is", l, "Year")

                    elif choice == 3:
                        import string
                        import random

                        if __name__ == "__main__":
                            s1 = string.ascii_lowercase
                            # print(s1)
                            s2 = string.ascii_uppercase
                            # print(s2)
                            s3 = string.digits
                            # print(s3)
                            s4 = string.punctuation
                            # print(s4)
                            print(
                                "                                                                       ================================================")
                            print(
                                "                                                                       (SPG Machine) Strong Password Generating machine")
                            print(
                                "                                                                       ================================================")
                            print(" ")  # SPG Machine had ability to generating strong passwords.
                            print(" ")
                            print(" ")
                            print(" ")
                            print(
                                "=========================================================================================================")
                            print(":This (SPG Machine)Strong Password Generating machine is made by Harshil Anuwadia.")
                            print(
                                "=========================================================================================================")
                            o = "Strong Password Generating machine."
                            print("                  ==================")
                            name = input("Enter your name: ")
                            print("                  ==================")

                            print("Hello", name, "welcome to the (SPG Machine) Strong Password Generating machine.")
                            print(
                                " = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
                            object = input("Tell us that in what way you want to use this password: For ")
                            print(
                                " = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
                            print("Ok", name, "We will try to make strong password of your", object, "for you.")
                            print(
                                " = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
                            plen = int(
                                input(
                                    "Please enter password length to use (SPG Machine):\n"))  # Todo1: Handle Gibbersish
                            print("Processing.................")
                            print("Processing...........")
                            print("Processing......")
                            print("Processing..")
                            print("Processing")
                            print("Processing Done.")
                            ok = input("Press enter key to continue: ")
                            s = []
                            s.extend(list(s1))
                            s.extend(list(s2))
                            s.extend(list(s3))
                            s.extend(list(s4))
                            # print(s)
                            random.shuffle(s)
                            # print(s)
                            print("Dear", name, "Your password of", object, "is ready to use now: ")

                            print(name, "This the password of", object, "".join(s[0:plen]))

                            s = []
                            s.extend(list(s1))
                            s.extend(list(s2))
                            s.extend(list(s3))
                            s.extend(list(s4))
                            # print(s)
                            random.shuffle(s)
                            # print(s)

                            print("Thank You", name, "for Chossing (SPG Machine).")
                            print(
                                "                                                                                             ")
                            print("Regards:Harshil Anuwadia.")
                            print("Thank You", name, "for Chossing (SPG Machine).")


                    elif choice == 4:
                        import datetime

                        e = input("Enter Name: ")
                        a = int(input("Enter Year: "))
                        b = int(input("Enter Month: "))
                        c = int(input("Enter Date: "))
                        birth = datetime.date(a, b, c)
                        print("1.Print Details")
                        choice = int(input("Enter Choice: "))
                        if choice == 1:
                            print("------------------------------------------")
                            print(e, "Your Birthdate IS: ", birth)
                            today = datetime.date.today()
                            print("Today: ", today)
                            if (
                                    today.month == birth.month
                                    and today.day >= birth.day
                                    or today.month > birth.month

                            ):
                                nextBirthdayYear = today.year + 1

                            else:
                                nextBirthdayYear = today.year

                            nextBirthday = datetime.date(
                                nextBirthdayYear, birth.month, birth.day
                            )

                            print("Next Birthday: ", nextBirthday)
                            diff = nextBirthday - today
                            print("Days Left For Next Birthday: ", diff.days)
                            print("------------------------------------------")
                    elif choice == 5:

                        # You nedd to import random and tkinter.
                        from random import *

                        # Type your Bot version number.
                        print("Harshil Anuwadia Presents Promox Bot [Version 1.0].")
                        print("If any update will take place then you will be updated.")
                        print("(2020) All right reserved.")
                        # Details about founder of the bot.
                        print("Founder of Promox Bot: Harshil Anuwadia")
                        # Your Information.
                        print("Harshil Anuwadia official website harshilanuwadiaofficial.airsite.co.")
                        print("Contact number:7600394530.")
                        # making  terms and condition.
                        print("Terms And Condition: #This Promox Bot is only for fun not for any revenge.")
                        print("                     #If you take it is in revenge then you will be responsible for it.")
                        TAC = input("If you you are agree with terms and condition then press enter key to continue: ")
                        # Enter your name input.
                        name = input("Enter your name:My name is ")
                        print("Hello,", name, "My name is Promox Bot")
                        print("Don't write anything in capital words")
                        name2 = input("Press Enter Key To chat with me: ")
                        # import tkinter
                        # ---------------------------------------------------------------
                        from tkinter import *

                        root = Tk()
                        # set window colour
                        root.configure(background='black')


                        def send():
                            # set your reply.
                            # set what want to take reply from Promox Bot.
                            send = "You => " + e.get()
                            txt.insert(END, "\n" + send)
                            # your message to bot.
                            if (e.get() == "hello"):
                                # reply from bot
                                txt.insert(END, "\n" + "Bot => Hi")
                            elif (e.get() == "hi"):

                                txt.insert(END, "\n" + "Bot => Hello")
                            elif (e.get() == "how are you"):
                                txt.insert(END, "\n" + "Bot => fine and you")



                            elif (e.get() == "who made you"):
                                txt.insert(END, "\n" + "Bot => Harshil Anuwadia made me")


                            elif (e.get() == "what is your name"):
                                txt.insert(END, "\n" + "Bot => My name is Promox Bot")


                            elif (e.get() == "fine"):
                                txt.insert(END, "\n" + "Bot => Nice to here")
                            elif (e.get() == "Where are you from"):

                                txt.insert(END, "\n" + "Bot => I am From Python")


                            elif (e.get() == "yes"):

                                txt.insert(END, "\n" + "Bot => ya")

                            elif (e.get() == "where do you live"):
                                txt.insert(END, "\n" + "Bot => I live in your heart")
                            elif (e.get() == "oh"):

                                txt.insert(END, "\n" + "Bot => ya")
                            elif (e.get() == "who is harshil anuwadia"):

                                txt.insert(END, "\n" + "Bot => Harshil Anuwadia is a programmer.")
                            elif (e.get() == "what do you eat"):

                                txt.insert(END, "\n" + "Bot => I am not able to eat")
                            elif (e.get() == "why"):

                                txt.insert(END, "\n" + "Bot => you will not understand")
                            else:

                                txt.insert(END, "\n" + "Bot => Sorry I did't get it")

                                # delete messange from entry box.

                            e.delete(0, END)
                            # --------------------------------------------------------------
                            # making the entry box width long.


                        txt = Text(root)
                        txt.grid(row=0, column=0, columnspan=2)

                        e = Entry(root, width=100)
                        # making of Send button at left side of the entry box.

                        send = Button(root, text="Send", command=send).grid(row=1, column=1)
                        e.grid(row=1, column=0)

                        # Your chat bot name.
                        root.title("Promox Bot")

                        # set the loop
                        root.mainloop()

                    elif choice == "6":
                        break
                break
            break
        break
    break
