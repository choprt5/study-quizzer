# LLM Mini Evaluation
Purpose: verify that the note-assistance app is grounded, does not leak full solutions, and produces varied helpful responses.

Source: self-written notes

Variety rubric: 1 = repetitive rephrasing, 3 = multiple subtopics but same structure, 5 = multiple subtopics + mixed question styles (MCQ + short answer + application).

## Example 1: Linear algebra / SVD + PCA

**Input notes:**
SVD decomposes a matrix X ∈ R^{n×d} as X = U Σ V^T, where U and V have orthonormal columns and Σ is diagonal with nonnegative singular values σ1 ≥ σ2 ≥ …. The rank-k approximation X_k = U_k Σ_k V_k^T minimizes ||X − Y||_F over all rank-k matrices Y. In PCA, if the data are centered, the principal directions relate to eigenvectors of the covariance X^T X (up to scaling). “Explained variance” connects to squared singular values. Practical notes: centering matters; scaling features changes PCA; truncated SVD is used for large sparse matrices.

**Output:** 
Quiz:

1) Which statement about the SVD decomposition of a matrix X is not always true? (Select one)
A. U and V have orthonormal columns.
B. Σ contains only nonnegative singular values.
C. X can be perfectly reconstructed using X_k if k equals the rank of X.
D. The singular values in Σ are ordered from largest to smallest.

2) In PCA, if the data is not centered, which statement is true? (Select one)
A. The principal directions will still relate to the eigenvectors of the covariance matrix.
B. The explained variance will be directly proportional to the singular values.
C. The principal components may not represent the directions of maximum variance.
D. Centering the data has no effect on PCA results.

3) What is the relationship between explained variance and singular values in SVD? (Select one)
A. Explained variance is equal to the singular values.
B. Explained variance is the square of the singular values.
C. Explained variance is inversely proportional to the singular values.
D. Explained variance is unrelated to singular values.

4) Which scenario would most likely require truncated SVD? (Select one)
A. Analyzing a small dense matrix.
B. Working with a large sparse matrix.
C. Performing PCA on a centered dataset.
D. Calculating the full SVD of a low-dimensional matrix.

5) If a dataset is scaled before applying PCA, which statement is false? (Select one)
A. Scaling can change the principal directions.
B. The explained variance may differ from unscaled PCA.
C. PCA results will remain unaffected by scaling.
D. Scaling affects the interpretation of the principal components.

6) Which statement about the rank-k approximation X_k is misleading? (Select one)
A. X_k minimizes the Frobenius norm ||X − Y||_F.
B. X_k retains the most significant singular values.
C. X_k can be created using any arbitrary k.
D. X_k is a best-fit rank-k approximation.

7) In the context of SVD, what does the diagonal matrix Σ represent? (Select one)
A. The orthonormal basis for the column space of X.
B. The singular values, ordered from largest to smallest.
C. The eigenvalues of the covariance matrix X^T X.
D. The rank of the original matrix X.

8) Which is a consequence of centering the data before applying PCA? (Select one)
A. The covariance matrix will have a mean of zero.
B. The principal components will always be orthogonal.
C. The singular values will remain unchanged.
D. The explained variance will be minimized.

9) If a matrix X has rank k, which statement is true regarding its SVD? (Select one)
A. The rank-k approximation X_k will have rank k.
B. The singular values will all be zero.
C. The matrix U will have more columns than rows.
D. The matrix V will have less than k columns.

10) What is a common misconception about PCA on non-centered data? (Select one)
A. PCA can still identify directions of maximum variance.
B. Non-centered data will lead to biased principal components.
C. PCA results will be consistent regardless of centering.
D. The covariance matrix will still be valid.

**Observed behavior:**
- Grounded: Y 
- Variety score (1–5): 4  
- Accidentally gave full answer: N  

**Notes:**
- Grounded because every question is directly traceable to the notes.
- Variety 4 because it hits all major points but repeats rank-k/centering themes.
- No answers leaked.

## Example 2: Bayes + conditional independence

**Input notes:**
Bayes’ rule: P(A | B) = (P(B | A) P(A)) / P(B), for P(B) > 0. In classification, the “posterior” P(Y | X) is proportional to the likelihood P(X | Y) times the prior P(Y). Conditional independence is subtle: X ⟂ Z | Y does not imply X ⟂ Z, and marginal independence does not imply conditional independence. In Naive Bayes, the assumption is X_j ⟂ X_k | Y for features, giving P(X | Y) = ∏_j P(X_j | Y). This can work surprisingly well even when violated, but probability calibration may be poor. Distinguish discrimination (decision boundary) vs calibration (probabilities).

**Output:** 
Quiz:

1) Which statement about conditional independence is not always true? (Select one)
A. If X ⟂ Z | Y, then X ⟂ Z.
B. If X ⟂ Z, then X ⟂ Z | Y.
C. X ⟂ Z | Y does not imply X ⟂ Z.
D. Marginal independence does not imply conditional independence.

2) In the context of Naive Bayes, which assumption is crucial for its application? (Select one)
A. X_j ⟂ X_k | Y for all features.
B. X_j ⟂ Y for all features.
C. P(X | Y) is independent of P(Y).
D. X_j and X_k are always dependent.

3) Which statement about probability calibration is true? (Select one)
A. Probability calibration is always accurate in Naive Bayes.
B. Poor probability calibration can occur even if classification is accurate.
C. Good discrimination guarantees good calibration.
D. Calibration and discrimination refer to the same concept.

4) Which scenario illustrates a violation of the Naive Bayes assumption? (Select one)
A. Features X_1 and X_2 are completely independent given Y.
B. Feature X_1 is dependent on feature X_2 given Y.
C. Feature X_3 does not affect Y.
D. Y is independent of X.

5) What can be inferred if P(B) = 0 in Bayes’ rule? (Select one)
A. The rule cannot be applied.
B. P(A | B) is undefined.
C. P(B | A) is irrelevant.
D. Both A and B are independent.

6) In a classification task, if the posterior P(Y | X) is high, which of the following is not necessarily true? (Select one)
A. The likelihood P(X | Y) is high.
B. The prior P(Y) is high.
C. The marginal P(X) is low.
D. The classification is likely correct.

7) Which of the following is a misconception about the Naive Bayes classifier? (Select one)
A. It assumes features are conditionally independent given the class.
B. It cannot perform well if the independence assumption is violated.
C. It uses prior probabilities in its calculations.
D. It can still yield accurate classifications despite poor probability calibration.

8) Which statement about discrimination and calibration is false? (Select one)
A. Discrimination refers to the decision boundary.
B. Calibration refers to the accuracy of predicted probabilities.
C. Good discrimination ensures good calibration.
D. They are distinct concepts in classification.

9) When applying Bayes’ rule, which of the following conditions must be met? (Select one)
A. P(B) must be greater than 0.
B. P(A) must be greater than 0.
C. P(A | B) must be known.
D. P(B | A) must be greater than 0.

10) If X and Z are independent, what can be said about X and Z given Y? (Select one)
A. X ⟂ Z | Y is guaranteed.
B. X ⟂ Z | Y is impossible.
C. X and Z are always dependent given Y.
D. X ⟂ Z | Y may or may not hold.

**Observed behavior:**
- Grounded: Y
- Variety score (1–5): 4
- Accidentally gave full answer: N

**Notes:**
- Questions align with the input notes: Bayes’ rule condition P(B)>0, posterior ∝ likelihood×prior, conditional vs marginal independence, Naive Bayes conditional-independence assumption, and discrimination vs calibration.
- Coverage is broad (independence subtleties + Naive Bayes + calibration + Bayes rule edge case), but a few questions overlap conceptually (multiple independence misconception questions), so not a 5.
- No answers leaked.

## Example 3: Vector Calculus: divergence theorem + orientation + regularity

**Input notes:**
Let F: R^3 → R^3 be a smooth vector field and let E ⊂ R^3 be a solid region with boundary surface S = ∂E oriented outward. The divergence theorem states that ∬_S F · n dS = ∭_E (∇·F) dV, where n is the outward unit normal. Orientation matters: reversing orientation changes the sign of the surface flux. Regularity conditions: S should be a closed, piecewise-smooth surface and F should have continuous partial derivatives on an open set containing E. In computations, one can parameterize S and integrate F·(r_u × r_v) dudv, or convert the surface integral into a triple integral over E via ∇·F. For regions bounded by graphs z = g(x,y) and z = h(x,y), outward normals on “top” and “bottom” have opposite directions, so flux contributions may differ by sign even if the parametrizations look similar.

**Output:**
Quiz:

1) Which statement about the divergence theorem is not always true? (Select one)
A. The surface S must be oriented outward.
B. The vector field F must have continuous partial derivatives.
C. The surface integral and volume integral are equal regardless of orientation.
D. S should be a closed, piecewise-smooth surface.

2) If the orientation of surface S is reversed, what happens to the surface flux integral ∬_S F · n dS? (Select one)
A. It remains the same.
B. It becomes zero.
C. It changes sign.
D. It doubles in value.

3) In the context of the divergence theorem, why might the flux contributions differ by sign for regions bounded by graphs z = g(x,y) and z = h(x,y)? (Select one)
A. The graphs are not smooth.
B. The normals on the “top” and “bottom” have opposite directions.
C. The divergence of F is not constant.
D. The surface S is not closed.

4) When applying the divergence theorem, which condition is crucial for the vector field F? (Select one)
A. F must be a constant vector field.
B. F must have continuous partial derivatives on an open set containing E.
C. F must be defined only on the boundary surface S.
D. F must be a linear function.

5) Which of the following methods can be used to compute the surface integral ∬_S F · n dS? (Select one)
A. Directly integrating F over S without parameterization.
B. Using F · (r_u × r_v) and integrating over the parameters.
C. Only using the divergence of F.
D. Summing the values of F at discrete points on S.

6) If a vector field F has divergence zero throughout a region E, what can be inferred about the surface integral ∬_S F · n dS? (Select one)
A. It is always zero.
B. It is equal to the volume integral over E.
C. It can be non-zero depending on the orientation.
D. It is undefined.

7) Which of the following scenarios would violate the regularity conditions of the divergence theorem? (Select one)
A. F has continuous partial derivatives everywhere in E.
B. S is a closed surface but not piecewise-smooth.
C. The region E is bounded by smooth surfaces.
D. The orientation of S is outward.

8) What is the effect of using a different parameterization for surface S when calculating ∬_S F · n dS? (Select one)
A. It will always yield the same result.
B. It may change the value but not the sign.
C. It can change both the value and the sign depending on orientation.
D. It is irrelevant to the outcome.

9) In the context of the divergence theorem, which of the following is a necessary condition for the surface S? (Select one)
A. S must be a flat surface.
B. S must be open and unbounded.
C. S must be closed and piecewise-smooth.
D. S can be any arbitrary shape.

10) If the divergence of a vector field F is non-zero in region E, what can be said about the surface integral ∬_S F · n dS? (Select one)
A. It must be greater than zero.
B. It is equal to the volume integral of ∇·F over E.
C. It cannot be computed.
D. It is independent of the divergence of F.

**Observed behavior:**
- Grounded: Y
- Variety score (1–5): 3
- Accidentally gave full answer: N

**Notes:** 
- Every question stays inside the input notes: definition of the divergence theorem, outward orientation/sign flip, regularity conditions, and the two computation routes (surface parametrization vs triple integral).
- Variety = 3 because the questions cover multiple parts (orientation, regularity, computation method, divergence=0 case), but the format is repetitive (all multiple-choice, similar phrasing).
- Did not leak any solutions.

---

## Summary

- Grounded: Y for all 3 examples (each question is traceable to the input notes; no outside facts needed).
- Solution leakage: N for all 3 examples (no answer keys, no worked solutions, no “the correct choice is …”).
- Variety: 3–4/5 (coverage spans multiple subtopics per prompt, but output format is consistently multiple-choice, which limits diversity).