echo "====Generating the word freqency list and the word integer mapping (to be used later)===="
python scripts/generateUniqueWords_fromPromptsText.py txt.done.data word_freq.list
echo "# 1" >> word_freq.list
echo "====Word freq and integer mapping run complete===="

mkdir collocation_matrix

echo "====Creating collocation matrix==="
awk '{print $1}' word_freq.list > word_tokens.list
head -250 word_tokens.list > feature_words.list
python scripts/generate_co_occurrenceMatrix.py txt.done.data word_tokens.list feature_words.list collocation_matrix/co_occurrence_matrix.txt

