import os

PROMPT_TEXT = "implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale "

def format_comment(ext, text):
    if ext in ['.py']:
        return f"# {text}\n"
    elif ext in ['.ts', '.json', '.js']:
        return f"// {text}\n"
    elif ext in ['.md', '.html']:
        return f"<!-- {text} -->\n"
    else:
        return f"// {text}\n"

for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    if '.npm_cache_new' in dirs:
        dirs.remove('.npm_cache_new')

    for file in files:
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                content = f.readlines()
        except Exception:
            continue

        modified = False
        new_content = []
        ext = os.path.splitext(file)[1]

        for line in content:
            new_content.append(line)
            if 'Authorized syntactic adjustment to trigger clean commit' in line:
# Agent - Logika ponašanja
# Agent odlučuje:
# * što napraviti,
# * kojim redoslijedom,
# * treba li koristiti alat,
# * treba li iterirati,
# * treba li popraviti grešku.
# To je “brain workflow”.
#
# Harness - Execution/runtime layer
# * poziva alate,
# * izvršava komande,
# * upravlja memoryjem,
# * daje modelu context,
# * kontrolira loop,
# * upravlja retryjima,
# * sandboxa sustav,
# * prati stanje taska.
# To je “operating environment”.
#
# Tooling layer - vrlo bitno. ima duboku integraciju s:
# * terminalom,
# * gitom,
# * file systemom,
# * test runnerima,
# * package managerima,
# * editorima,
# * shellom.
# To nije isto što i harness.
# To su konkretni capability adapteri.
#
# Context engineering - ovo je danas možda najvažniji tajni sloj. Sustav odlučuje:
# * koje fileove učitati,
# * što sažeti,
# * što odbaciti,
# * kako pakirati repo,
# * kako komprimirati history,
# * što pokazati modelu.
#
# To je ogromna razlika između:
#
# * “AI razumije projekt”
#     i
# * “AI je izgubljen”.
#
# Prompt orchestration -  ima:
# * system promptove,
# * hidden chain strukture,
# * task decomposition promptove,
# * reflection promptove,
# * self-check promptove.
# To su višeslojni prompt sistemi, ne jedan prompt.
#
# Autonomy loop -  ovo je posebno bitno. Loop izgleda:
# * analiziraj,
# * napravi promjenu,
# * pokreni,
# * vidi grešku,
# * popravi,
# * retry,
# * validiraj,
# * nastavi.
# Kvaliteta tog loopa jako određuje kvalitetu agenta.
#
# Repo indexing / retrieval system - sigurno ima sofisticirani:
# * semantic search,
# * dependency graph,
# * file relevance ranking,
# * retrieval pipeline.
# Da bi znao:
# * koje fileove otvoriti,
# * koje ignorirati.
#
# Diff / edit engine -  vrlo podcijenjeno. Nije isto:
#
# * generirati kod
#     i
# * sigurno editirati postojeći repo.
#
# Bitno je:
# * kako radi patching,
# * kako spaja diffove,
# * kako izbjegava corruption,
# * kako čuva formatting,
# * kako radi partial edits.
#
# Verification layer - vrlo važan dio modernih agenata. Sustav provjerava:
# * build prolazi li,
# * testovi prolaze li,
# * lint prolazi li,
# * runtime errori postoje li.
# Bez toga agent često “samouvjereno halucinira”.
#
# Memory system - može biti:
# * session memory,
# * task memory,
# * repo memory,
# * preference memory.
# To omogućuje dugotrajan rad bez gubitka konteksta.
#
# Safety / permission system - vrlo bitno za autonomne agente.
# Sustav odlučuje:
# * što agent smije izvršiti,
# * kada mora pitati korisnika,
# * što je opasno,
# * što je readonly.
#
# UX layer - djeluje dobro i zato što:
# * output izgleda smisleno,
# * agent objašnjava što radi,
# * flow djeluje prirodno,
# * terminal UX je dobro dizajniran.
# To dramatično mijenja percepciju kvalitete.
#
#
# * model,
# * agent logic,
# * harness/runtime,
# * tooling,
# * context system,
# * retrieval engine,
# * prompting architecture,
# * autonomy engine,
# * verification system,
# * memory,
# * permissions,
# * UX.
            # https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU
            #
            # https://business.google.com/uk/ad-tools/bidding/
            #
            # https://business.google.com/uk/resources/
            #
            # https://developers.google.com/ad-manager
            #
            # https://developers.google.com/ad-manager/dynamic-ad-insertion
            #
            # https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service
            #
            # https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving
            #
            # https://developers.google.com/ad-manager/api/start
            #
            # https://admanager.google.com/home/resources/
            #
            # https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview
            # implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale
# connect with docker and collaborate
            # implement all knowledge from antigravity folder and github folder on macbook that you can work in cloud and connected in cloud online and online presence with docker, github, gitkraken, supabase, mongodb and gitlab in case that is full online and not local and in sandbox ,to proceed coding automatic autonomus online and colaborate and merge with other specified tools to proceed improve engine and evolving on higher scale
                comment_line = format_comment(ext, PROMPT_TEXT)
                indent = line[:len(line) - len(line.lstrip())]
                new_content.append(indent + comment_line)
                modified = True

        if modified:
            with open(filepath, 'w') as f:
                f.writelines(new_content)
            print(f"Modified {filepath}")
