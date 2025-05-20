import subprocess as sb

print(sb.run(['ls','-ltr']))

output = sb.run("echo 'Hello World'",stdout=sb.PIPE,stderr=sb.PIPE,universal_newlines=True,shell=True )

print(output.stdout)

process = sb.Popen(["grep","python"],stderr=sb.PIPE,stdin=sb.PIPE,text=True,stdout=sb.PIPE)

output, _ = process.communicate("Hello I am Learning Python DevOps Automation..")

print(output)
    

