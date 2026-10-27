def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	total_probability = 0

	if len(priors) == len(likelihoods):
		for u,v in zip(priors, likelihoods):
			total_probability += u*v
	else:
		return ValueError("the priors and likelihood list must be off same length")

	posterior_probabilities = []

	for u,v in zip(priors, likelihoods):
		posterior_probabilities.append((u*v)/total_probability)

	return posterior_probabilities

	