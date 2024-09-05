import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# إنشاء البيئة
env = gym.make('CartPole-v1')
state_size = env.observation_space.shape[0]
action_size = env.action_space.n

# بناء نموذج DQN
model = Sequential()
model.add(Dense(24, input_dim=state_size, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(action_size, activation='linear'))
model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))

# إعدادات Q-learning
gamma = 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01
episodes = 1000

# حلقة التدريب
for e in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    for time in range(500):
        if np.random.rand() <= epsilon:
            action = np.random.choice(action_size)
        else:
            action = np.argmax(model.predict(state, verbose=0)[0])

        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        target = reward
        if not done:
            target = (reward + gamma * np.amax(model.predict(next_state, verbose=0)[0]))

        target_f = model.predict(state, verbose=0)
        target_f[0][action] = target

        model.fit(state, target_f, epochs=1, verbose=0)
        state = next_state
        if done:
            print(f'episode: {e}/{episodes}, score: {time}, epsilon: {epsilon:.2}')
            break

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay
