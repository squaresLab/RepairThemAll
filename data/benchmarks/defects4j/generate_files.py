import subprocess
import json

def equals_dict(src_dict1, src_dict2):
    if src_dict1.keys() != src_dict2.keys():
        return False

    for key in src_dict1.keys():
        if src_dict1[key] != src_dict2[key]:
            return False

    return True

def foo(project_name, bug_num_list, package, url):
    data_dict = { 
        "classpath": {}, 
        "complianceLevel": {}, 
        "libs": [
        ], 
        "project": project_name,
        "nbBugs": len(bug_num_list), 
        "package": package, 
        "src": {}, 
        "url": url
    }

    curr_cp = None
    curr_src = None
    prev_bug_num = -1

    for bug_num in bug_num_list:
        print(bug_num)
        data_dict['complianceLevel'][str(bug_num)] = {
            "source":8,
            "target":8
        }

        cmd = "bash get_paths.sh %s %s" % (project_name, str(bug_num))
        print(cmd)
        subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)

        with open('%s%s/paths.data' % (project_name, str(bug_num))) as f:
            lines = f.readlines()
            testdir = lines[0].strip()
            srcdir = lines[1].strip()
            srcbin = lines[2].strip()
            testbin = lines[3].strip()

        src_data = {
            "binjava": srcbin, 
            "bintest": testbin, 
            "srcjava": srcdir, 
            "srctest": testdir
        }
        cp_data = "%s:%s" % (srcbin, testbin)

        if curr_cp is None:
            curr_cp = cp_data
        if curr_src is None:
            curr_src = src_data

        if curr_cp != cp_data or not equals_dict(curr_src, src_data):
            data_dict['classpath'][str(prev_bug_num)] = curr_cp
            data_dict['src'][str(prev_bug_num)] = curr_src

            curr_cp = cp_data
            curr_src = src_data

        prev_bug_num = bug_num

    data_dict['classpath'][str(bug_num_list[-1])] = curr_cp
    data_dict['src'][str(bug_num_list[-1])] = curr_src

    return data_dict

if __name__ == '__main__':


    with open('new_data/chart.json', 'w') as f:
        bugs = list(range(1,27))
        json.dump(
            foo('Chart', bugs, "org.jfree", "https://github.com/jfree/jfreechart-fse"), 
            f,
            indent=3)


    with open('new_data/closure.json', 'w') as f:
        bugs = list(range(1,63)) + list(range(64,93)) + list(range(94,177))
        json.dump(
            foo('Closure', bugs, "com.google", "https://github.com/google/closure-compiler"), 
            f,
            indent=3)

    with open('new_data/cli.json', 'w') as f:
        bugs = list(range(1,6)) + list(range(7,41))
        json.dump(
            foo('Cli', bugs, "org.apache.commons", "https://github.com/apache/commons-cli"), 
            f,
            indent=3)


    with open('new_data/codec.json', 'w') as f:
        bugs = list(range(1,19))
        json.dump(
            foo('Codec', bugs, "org.apache.commons", "https://github.com/apache/commons-codec"), 
            f,
            indent=3)



    with open('new_data/collections.json', 'w') as f:
        bugs = list(range(25,29))
        json.dump(
            foo('Collections', bugs, "org.apache.commons", "https://github.com/apache/commons-collections"), 
            f,
            indent=3)



    with open('new_data/compress.json', 'w') as f:
        bugs = list(range(1,48))
        json.dump(
            foo('Compress', bugs, "org.apache.commons", "https://github.com/apache/commons-compress"), 
            f,
            indent=3)

    with open('new_data/csv.json', 'w') as f:
        bugs = list(range(1,17))
        json.dump(
            foo('Csv', bugs, "org.apache.commons", "https://github.com/apache/commons-csv"), 
            f,
            indent=3)

    with open('new_data/gson.json', 'w') as f:
        bugs = list(range(1,19))
        json.dump(
            foo('Gson', bugs, "com.google", "https://github.com/google/gson"), 
            f,
            indent=3)

    with open('new_data/jacksoncore.json', 'w') as f:
        bugs = list(range(1,27))
        json.dump(
            foo('JacksonCore', bugs, "com.fasterxml", "https://github.com/FasterXML/jackson-core"), 
            f,
            indent=3)

    with open('new_data/jacksondatabind.json', 'w') as f:
        bugs = list(range(1,113))
        json.dump(
            foo('JacksonDatabind', bugs, "com.fasterxml", "https://github.com/FasterXML/jackson-databind"), 
            f,
            indent=3)

    with open('new_data/jacksonxml.json', 'w') as f:
        bugs = list(range(1,7))
        json.dump(
            foo('JacksonXml', bugs, "com.fasterxml", "https://github.com/FasterXML/jackson-dataformat-xml"), 
            f,
            indent=3)

    with open('new_data/jsoup.json', 'w') as f:
        bugs = list(range(1,94)) 
        json.dump(
            foo('Jsoup', bugs, "org.jsoup", "https://github.com/jhy/jsoup"), 
            f,
            indent=3)

    with open('new_data/jxpath.json', 'w') as f:
        bugs = list(range(1,23)) 
        json.dump(
            foo('JxPath', bugs, "org.apache.commons", "https://github.com/apache/commons-jxpath"), 
            f,
            indent=3)

    with open('new_data/lang.json', 'w') as f:
        bugs = list(range(1,2)) + list(range(3,66))
        json.dump(
            foo('Lang', bugs, "org.apache.commons", "https://github.com/apache/commons-lang"), 
            f,
            indent=3)

    with open('new_data/math.json', 'w') as f:
        bugs = list(range(1,107))
        json.dump(
            foo('Math', bugs, "org.apache.commons", "https://github.com/apache/commons-math"), 
            f,
            indent=3)

    with open('new_data/mockito.json', 'w') as f:
        bugs = list(range(1,39))
        json.dump(
            foo('Mockito', bugs, "org.mockito", "https://github.com/mockito/mockito"), 
            f,
            indent=3)

    with open('new_data/time.json', 'w') as f:
        bugs = list(range(1,21)) + list(range(22,28))
        json.dump(
            foo('Time', bugs, "org.joda", "https://github.com/JodaOrg/joda-time"), 
            f,
            indent=3)