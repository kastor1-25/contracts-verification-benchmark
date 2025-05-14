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
        
        const signers = await ethers.getSigners();

        const payees = [
            signers[0].address,
            signers[1].address,
            signers[2].address];

        const PaymentSplitter2 = await(ethers.deployContract("PaymentSplitter", [
            payees,
            [1,1,1]
        ],
        {
            value: ethers.parseUnits("2", "wei")
        }));
        return { PaymentSplitter, RevertOnReceive , PaymentSplitter2, payees};
    };



    // These revert, so I don't think they are useful

    it("release when funds are insufficient for a fair split should fail", async function() {
        const { PaymentSplitter2, payees } = await loadFixture(deployContract);
        const balanceBefore = await PaymentSplitter2.balanceOf(PaymentSplitter2.getAddress());
       
        await PaymentSplitter2.release(payees[0]);
        expect(await PaymentSplitter2.balanceOf(PaymentSplitter2.getAddress())).not.to.equal(balanceBefore);
    })

    it("release but it reverts", async function () {
        const { PaymentSplitter, RevertOnReceive } = await loadFixture(deployContract);
        
        const balanceBefore = await PaymentSplitter.balanceOf(PaymentSplitter.getAddress());
        await(PaymentSplitter.release(RevertOnReceive.getAddress()));
        expect(await PaymentSplitter.balanceOf(PaymentSplitter.getAddress())).not.to.equal(balanceBefore);
    });
});