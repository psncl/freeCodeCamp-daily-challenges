function costToFill(tankSize, fuelLevel, pricePerGallon) {
  const amount = (tankSize - fuelLevel) * pricePerGallon;
  const formattedAmount = amount.toFixed(2);
  const str = `$${formattedAmount}`;
  return str;
}
