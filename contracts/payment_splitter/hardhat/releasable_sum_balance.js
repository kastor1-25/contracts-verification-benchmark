
const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

const { expect } = require("chai");

describe("PaymentSplitter", function () {

    async function deployContract() {
        const signers = await ethers.getSigners();

        const payees = [
            signers[0].address,
            signers[1].address,
            signers[2].address];

        const PaymentSplitter = await(ethers.deployContract("PaymentSplitter", [
            payees,
            [1,1,1]
        ],
        {
            value: ethers.parseUnits("4", "wei")
        }));

        return { PaymentSplitter };
    };

    it ("Releasable sum balance", async function() {
        const { PaymentSplitter} = await loadFixture(deployContract);
        const balance = await PaymentSplitter.balanceOf(PaymentSplitter.getAddress());    
        const totalReleasable = await PaymentSplitter.getTotalReleasable();
        
        expect(totalReleasable).to.equal(balance);
    })
});