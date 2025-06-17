class Customer {
  constructor(private name: string) {}

  greet(): void {
    console.log("Hello, " + this.name);
  }
}

class VIPCustomer extends Customer {
  getDiscount(): number {
    return 20;
  }
}
