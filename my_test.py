import my_debugger

debugger = my_debugger.debugger()

pid = raw_input("Enter the PID of the process to attach to: ")

debugger.attach(int(pid))

list = debugger.enumerate_threads()

# For each thread in the list we want to
# grab the value of each of the registers
for thread in list:
    thread_context = debugger.get_thread_context(thread)

    # Now let's output the contents of some of the registers
    print "[*] Dumping registers for thread ID: 0x%08x" %thread
    print "[**] EIP: 0x%08x" % thread_context.Eip
    print "[**] EIP: 0x%08x" % thread_context.Esp
    print "[**] EIP: 0x%08x" % thread_context.Ebp
    print "[**] EIP: 0x%08x" % thread_context.Eax
    print "[**] EIP: 0x%08x" % thread_context.Ebx
    print "[**] EIP: 0x%08x" % thread_context.Ecx
    print "[**] EIP: 0x%08x" % thread_context.Edx
    print "[*] END DUMP"
     
debugger.detach()