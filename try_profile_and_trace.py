import sys
import dis
import numpy as np

# from skimage import data
# from skimage.feature import Cascade
import inspect


# # Load the trained file from the module root.
# trained_file = data.lbp_frontal_face_cascade_filename()

# # Initialize the detector cascade.
# detector = Cascade(trained_file)

# img = data.astronaut()
# __ltrace__ = True


def tracer(frame, event, arg):
    # frame.f_trace_opcodes = True
    # if event == 'call' or event == 'c_call':
    #     print(inspect.getframeinfo(frame))
    #     print("\n\n")
    # print("tracer", event, arg)
    print("tracer", event, arg, inspect.getframeinfo(frame))
    bytecode = dis.Bytecode(frame.f_code)
    print(bytecode.info())
    print(bytecode.dis())
    print("\n\n")
    return tracer

def profiler(frame, event, arg):
    if event not in {'call', 'c_call'}:
        return
    # frame.f_trace_opcodes = True
    code = frame.f_code
    print(arg)
    print("consts", code.co_consts)
    print("names", code.co_names)
    print("varnames", code.co_varnames)
    # print("profiler", event, arg, inspect.getframeinfo(frame))

    # if event == 'call' or event == 'c_call':
    #     print(inspect.getframeinfo(frame))
    #     print("\n\n")
    # print(event, arg, inspect.getframeinfo(frame))
    bytecode = dis.Bytecode(code)
    # print(frame, frame.f_lasti)
    print(bytecode.info())
    print(bytecode.dis())
    # print("\n\n")


def fn():
    x = np.arange(10)
    # np.arange(10)
    z = 10
    # np.arange(z)
    x.reshape((2, 5))
    x.reshape((5, 2))
    x.reshape((10, 1))
    # y = x[0:2] + x[2:4]
    # z = np.power(y, 10)
    # z = np.power(x, y)
    # z * 10000
    # print(z)
    # print("SCIIKIT")
    # detected = detector.detect_multi_scale(
    #     img=img, scale_factor=1.2, step_ratio=1, min_size=(60, 60), max_size=(123, 123)
    # )
    # print("DONE")


# import cProfile

# cProfile.run('fn()')

# sys.settrace(tracer)
sys.setprofile(profiler)
fn()
# sys.settrace(None)
sys.setprofile(None)
