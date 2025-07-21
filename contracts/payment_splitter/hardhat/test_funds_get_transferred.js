const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");

describe("PaymentSplitter", function () {
    async function deployContract() {
        const RevertOnReceive = await(ethers.deployContract("RevertOnReceive"))

        const PaymentSplitter = await(ethers.deployContract("PaymentSplitter", [
            [RevertOnReceive.getAddress()],
            [1]
        ],
        {
            value: ethers.parseUnits("100", "wei")
        }));

        return { PaymentSplitter, RevertOnReceive };
    };

    it("Transfer Reverts", async function () {
        const { PaymentSplitter, RevertOnReceive } = await loadFixture(deployContract);
        
        const balanceBefore = await PaymentSplitter.balanceOf(PaymentSplitter.getAddress());

        await expect(
            PaymentSplitter.release(RevertOnReceive.getAddress())
            ).to.be.reverted;

        const balanceAfter = await PaymentSplitter.balanceOf(PaymentSplitter.getAddress());

        expect(balanceAfter).to.equal(balanceBefore);
    });
})