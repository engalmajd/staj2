import gym
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

env = gym.make('CartPole-v1', render_mode='rgb_array')

state = env.reset()
done = False

plt.ion()
fig, ax = plt.subplots()
img = ax.imshow(env.render())

while not done:
    action = env.action_space.sample()
    state, reward, done, truncated, info = env.step(action)
    done = done or truncated

    img.set_data(env.render())
    plt.pause(0.001)
    clear_output(wait=True)
    display(fig)

env.close()
plt.ioff()
