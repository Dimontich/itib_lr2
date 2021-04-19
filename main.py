import math
import matplotlib.pyplot as plt


def fun(x):
    return math.log(x) - 1


def net(x, w, w_0):
    net = w_0
    for (k, j) in zip(x, w):
        net += k * j
    return net


a = 1
b = 5
norm_education = 1
k = [5, 6, 7]  # размер окна
epochs_count = [1000, 2000, 3000]
points = [a]


def n(a, b, norm_education, k, epochs_count):
    save = epochs_count
    points = [a]
    true_answers = [fun(a)]
    delta = (b - a) / 19
    c = 2 * b - a

    while a < c:
        a += delta
        true_answers.append(fun(a))
        points.append(a)

    answer = []
    w = [0] * (k + 1)
    while epochs_count != 0:
        for i in range(k, 20):
            f_net = net(true_answers[i - k: i - 1], w[1:], w[0])
            sigma = true_answers[i] - f_net
            for j in range(1, k + 1):
                w[j] += norm_education * sigma * true_answers[i - k + j - 1]
        eps = 0

        neural_answers = true_answers[:k]
        l = len(true_answers)
        for i in range(k, l):
            f_net = net(neural_answers[i - k: i - 1], w[1:], w[0])
            neural_answers.append(f_net)
            eps += (true_answers[i] - net(true_answers[i - k: i - 1], w[1:], w[0])) ** 2
        esp = math.sqrt(eps)
        answer.append([save, neural_answers, true_answers, points, w, esp, k])
        epochs_count -= 1

    return answer


answer = []
for i in k:
    for j in epochs_count:
        answer.append(n(a, b, norm_education, i, j))

for i in answer:
    print('=================================================================================|')
    _, ax = plt.subplots()
    ax.plot(i[-1][3], i[-1][2], label='Реальная функция')
    ax.plot(i[-1][3], i[-1][1], label='Прогноз')
    ax.legend()
    plt.xlabel("x")  # ось абсцисс
    plt.ylabel("Реальная функция, Прогноз")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.show()
    print('| window size = ', i[-1][6], ' |   epochs = ', i[-1][0], ' |  summary error = ', i[-1][5], '  |',
          '\n|________________________________________________________________________________|',
          '\n| Weights =                                                                      |')
    for (j, k) in zip(i[-1][4], range(0, len(i[-1][4]))):
        a = list(str(j))
        tab = 59 - len(a)
        print(f'|            w[{k}] = {j}', ' ' * tab, '|',)
    print('|________________________________________________________________________________|',
          '\n|================================================================================|\n\n\n')
