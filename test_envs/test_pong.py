import ale_py
import gymnasium as gym

gym.register_envs(ale_py) 

# Create environment
env = gym.make("ALE/Pong-v5", render_mode="human")  # render_mode="human" to visualize
# replace "CartPole-v1" with "ALE/Pong-v5" to play Pong or any other env

# Reset environment
obs, info = env.reset()
done = False

while not done:
    env.render()
    action = env.action_space.sample()  # random action
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

    print(f"Reward: {reward}, Info: {info}")

env.close()
