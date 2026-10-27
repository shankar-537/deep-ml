def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	
	if len(priors) == len(likelihoods):
		total_probability = sum(u*v for u,v in zip(priors, likelihoods))
	else:
		return ValueError("the priors and likelihood list must be off same length")

	posterior_probabilities = [(u*v)/total_probability for u,v in zip(priors,likelihoods)]
	
	return posterior_probabilities

	