using Microsoft.ML;
using System;

public class Predictor
{
    public class SentimentData
    {
        public string Text { get; set; } = "";
    }

    public class SentimentPrediction : SentimentData
    {
        public bool Prediction { get; set; }
        public float Probability { get; set; }
        public float Score { get; set; }
    }

    public static void Main(string[] args)
    {
        var context = new MLContext();
        ITransformer model = context.Model.Load("sentiment_model.zip", out _);
        var predEngine = context.Model.CreatePredictionEngine<SentimentData, SentimentPrediction>(model);

        Console.WriteLine("Yorum girin (çıkmak için boş bırakıp enter'a basın):");
        while (true)
        {
            Console.Write("> ");
            string input = Console.ReadLine();
            if (string.IsNullOrWhiteSpace(input))
                break;

            var sample = new SentimentData { Text = input };
            var prediction = predEngine.Predict(sample);

            Console.WriteLine($"Tahmin: {(prediction.Prediction ? "Pozitif 😊" : "Negatif 😞")}, Olasılık: {prediction.Probability:P2}");
        }
    }
}
