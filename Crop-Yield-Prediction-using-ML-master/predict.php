<?php 
// Enable error reporting (for development)
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Get data from URL
$state = $_GET['state'] ?? '';
$lga = $_GET['lga'] ?? '';
$crop = $_GET['crop'] ?? '';
$area = $_GET['area'] ?? '';
$soil = $_GET['soil'] ?? '';

// Run Python model with safe argument escaping
$command = "python RF_predict.py " 
    . escapeshellarg($state) . " " 
    . escapeshellarg($crop) . " " 
    . escapeshellarg($area) . " " 
    . escapeshellarg($soil);
$output = shell_exec($command);

// Clean and parse output
$output = trim($output);

if (!empty($output)) {
    $parts = explode('|', $output);
    $predicted_yield = (isset($parts[0]) && is_numeric($parts[0])) 
        ? number_format((float)$parts[0], 2) 
        : 'Unavailable';
    $warning_message = trim($parts[1] ?? '');
} else {
    $predicted_yield = 'Unavailable';
    $warning_message = '';
}

// Soil NPK + pH values
$soil_data = [
  "loamy" => ["N" => 90, "P" => 40, "K" => 40, "ph" => 6.5],
  "sandy" => ["N" => 60, "P" => 30, "K" => 35, "ph" => 5.8],
  "clay"  => ["N" => 75, "P" => 45, "K" => 50, "ph" => 6.8]
];

$nitrogen = isset($soil_data[$soil]) ? $soil_data[$soil]["N"] . "%" : 'N/A';
$phosphorus = isset($soil_data[$soil]) ? $soil_data[$soil]["P"] . "%" : 'N/A';
$potassium = isset($soil_data[$soil]) ? $soil_data[$soil]["K"] . "%" : 'N/A';
$ph = isset($soil_data[$soil]) ? $soil_data[$soil]["ph"] : 'N/A';

// Simulate or fallback weather values (optional)
$temperature = rand(24, 30);
$humidity = rand(75, 95);
$rainfall = rand(100, 250);
?>

<div class="result-card p-3" style="background-color: #f7f7f7; border-radius: 10px;">
  <h4 class="text-success">✅ Yield Prediction Result</h4>
  <p><strong>📍 Location:</strong> <?php echo htmlspecialchars($state); ?>, <?php echo htmlspecialchars($lga); ?></p>
  <p><strong>🌱 Soil Type:</strong> <?php echo htmlspecialchars($soil); ?></p>
  <p><strong>🌾 Crop:</strong> <?php echo htmlspecialchars($crop); ?></p>
  <p><strong>📐 Area:</strong> <?php echo htmlspecialchars($area); ?> acres</p>
  <p><strong>🌡️ Temperature:</strong> <?php echo $temperature; ?> °C</p>
  <p><strong>💧 Humidity:</strong> <?php echo $humidity; ?>%</p>
  <p><strong>☔ Rainfall:</strong> <?php echo $rainfall; ?> mm</p>
  <p><strong>📊 Estimated Yield:</strong> <?php echo $predicted_yield; ?> tons</p>

  <?php if (!empty($warning_message)) : ?>
    <div class="alert alert-warning mt-3">
      ⚠️ <?php echo htmlspecialchars($warning_message); ?>
    </div>
  <?php endif; ?>

  <hr>
  <h5 class="text-primary">🧪 Soil Nutrient Details</h5>
  <p>🟢 Nitrogen (N): <?php echo $nitrogen; ?></p>
  <p>🟠 Phosphorus (P): <?php echo $phosphorus; ?></p>
  <p>🟡 Potassium (K): <?php echo $potassium; ?></p>
  <p>⚖️ Soil pH: <?php echo $ph; ?></p>
</div>
