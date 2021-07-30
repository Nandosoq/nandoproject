def my_mean(samples):
    return sum(samples) / len(samples)

def my_standard_deviation(samples):
    mean = my_mean(samples)
    a = 0
    for i in samples:
        a += (i - mean)**2
    return (a / (len(samples) - 1))**(1 / 2)


def my_median(samples):
    samples.sort()

    if len(samples)%2 ==1:
        return samples[int(len(samples)/2)]
    return (samples[int(len(samples)/2)-1] + samples[int(len(samples)/2)])/2


def my_mode(samples):
    a=0
    value=0
    for i in samples:
        if samples.count(i)>a:
            a = samples.count(i)
            value = i
            print(a)
            print(value)
    return value
