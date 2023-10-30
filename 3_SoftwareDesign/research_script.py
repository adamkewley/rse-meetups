import numpy as np
import matplotlib.pyplot as plt

def target_distribution(x):
    # Define the target distribution, which is a 2D Gaussian in this example.
    mean = np.array([2.0, 2.0])
    cov = np.array([[1.0, 0.8], [0.8, 1.0]])
    inv_cov = np.linalg.inv(cov)
    exponent = -0.5 * np.dot(np.dot((x - mean), inv_cov), (x - mean).T)
    return np.exp(exponent)

def slice_sampling(num_samples, initial_state, width=1.0):
    samples = [initial_state]
    current_state = initial_state

    for _ in range(num_samples):
        # Sample a new state using Slice Sampling.
        y = current_state + width * np.random.randn(len(current_state))
        u = np.random.uniform(0, 1)
        left, right = current_state, current_state

        while target_distribution(left) > u * target_distribution(y):
            left -= width
        while target_distribution(right) > u * target_distribution(y):
            right += width

        current_state = left + np.random.rand() * (right - left)

        samples.append(current_state)

    return np.array(samples)

def metropolis_hastings(num_samples, initial_state, proposal_std):
    samples = [initial_state]
    current_state = initial_state

    for _ in range(num_samples):
        # Propose a new state from a normal distribution (random walk proposal).
        proposal = np.random.normal(current_state, proposal_std, size=len(current_state))

        # Calculate acceptance ratio.
        acceptance_ratio = min(1.0, target_distribution(proposal) / target_distribution(current_state))

        # Accept or reject the proposal based on the acceptance ratio.
        if np.random.uniform(0, 1) < acceptance_ratio:
            current_state = proposal

        samples.append(current_state)

    return np.array(samples)

def proposal_distribution(x):
    # Define the proposal distribution, which is another Gaussian distribution.
    proposal_mean = np.array([0.0, 0.0])
    proposal_cov = np.array([[1.0, 0.0], [0.0, 1.0]])
    inv_proposal_cov = np.linalg.inv(proposal_cov)
    exponent = -0.5 * np.dot(np.dot((x - proposal_mean), inv_proposal_cov), (x - proposal_mean).T)
    return np.exp(exponent)

def importance_sampling(num_samples):
    samples = np.zeros((num_samples, 2))
    importance_weights = np.zeros(num_samples)

    for i in range(num_samples):
        sample = np.random.multivariate_normal([0, 0], np.eye(2))  # Sample from the proposal distribution
        importance_weights[i] = target_distribution(sample) / proposal_distribution(sample)
        samples[i] = sample

    estimated_mean = np.mean(importance_weights * np.sum(samples, axis=1))
    return samples, importance_weights, estimated_mean

def rejection_sampling(num_samples):
    samples = []
    for _ in range(num_samples):
        while True:
            sample = np.random.uniform([-1.0, -1.0], [5.0, 5.0])  # Sample from the proposal distribution
            acceptance_prob = target_distribution(sample) / (1.5 * 1.5)  # Adjusted for the bounding box size
            if np.random.uniform(0, 1) < acceptance_prob:
                samples.append(sample)
                break
    return np.array(samples)

def gibbs_sampling(num_samples, initial_state, mean, cov):
    samples = [initial_state]
    current_state = initial_state

    for _ in range(num_samples):
        # Sample from the conditional distribution of X1 given X2.
        x1_mean = mean[0] + cov[0, 1] / cov[1, 1] * (current_state[1] - mean[1])
        x1_cov = cov[0, 0] - cov[0, 1] ** 2 / cov[1, 1]
        current_state[0] = np.random.normal(x1_mean, np.sqrt(x1_cov))

        # Sample from the conditional distribution of X2 given X1.
        x2_mean = mean[1] + cov[0, 1] / cov[0, 0] * (current_state[0] - mean[0])
        x2_cov = cov[1, 1] - cov[0, 1] ** 2 / cov[0, 0]
        current_state[1] = np.random.normal(x2_mean, np.sqrt(x2_cov))

        samples.append(current_state.copy())

    return np.array(samples)

num_samples = 1000
initial_state = np.array([0.0, 0.0])
mean = np.array([2.0, 2.0])
cov = np.array([[1.0, 0.8], [0.8, 1.0]])
proposal_std = 0.5

# change this to change the algorithm
if False:
    title = "Metropolis-Hastings Sampling"
    samples = metropolis_hastings(num_samples, initial_state, proposal_std)
elif False:
    title = "Slice Sampling"
    samples = slice_sampling(num_samples, initial_state)
elif False:
    title = "Importance Sampling"
    samples, _, _ = importance_sampling(num_samples)
elif False:
    title = "Rejection Sampling"
    samples = rejection_sampling(num_samples)
else:
    title = "Gibbs Sampling"
    samples = gibbs_sampling(num_samples, initial_state, mean, cov)

plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5, s=5)
plt.title(title)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
