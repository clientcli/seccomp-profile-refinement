SYSDIGERR = -1
NOPROCESS = -2
NOFUNCS = -3
NOATTACH = -4
CONSTOP = -5
HSTOPS = -6
HLOGLEN = -7
HNOKILL = -8
HNORUN = -9
CACHE = ".cache"
LIBFILENAME = "libs.out"
LANGFILENAME = ".lang.cache"
BINLISTCACHE = ".binlist.cache"
LIBLISTCACHE = ".liblist.cache"
TOOLNAME = "CONFINE"

ERRTOMSG = dict()
ERRTOMSG[SYSDIGERR] = "There was an error running sysdig, please make sure it is installed and the script has enough privileges to run it"
ERRTOMSG[NOPROCESS] = "Sysdig was not able to identify any processes. This causes our dynamic analysis to fail and the static analysis cannot analyze anything"
ERRTOMSG[NOFUNCS] = "No imported functions could be extracted from any of the binaries and libraries required by the container"
ERRTOMSG[NOATTACH] = "The container did not run in attached mode"
ERRTOMSG[CONSTOP] = "The container got killed after being launched in attach mode"
ERRTOMSG[HSTOPS] = "The hardened container stops running. Probably due to a problem in generating the SECCOMP profile and prohibiting access to a required system call"
ERRTOMSG[HLOGLEN] = "While the container has been hardened successfully, the log length doesn't match the original log length, which was run without any SECCOMP profile"
ERRTOMSG[HNOKILL] = "The container has been hardened successfully, but we could not kill it afterwards. This usually means that the container has died. If so, the generated profile has a problem"
ERRTOMSG[HNORUN] = "The hardened container does not run at all. The generated SECCOMP profile has a problem"
