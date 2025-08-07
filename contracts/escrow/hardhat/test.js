const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

const { expect } = require("chai");

describe("Escrow", function () {

    async function deployContract() {
        const [buyer, seller, arbiter] = await ethers.getSigners();
        const fee = ethers.parseUnits("10", "wei");

        const Escrow = await(ethers.deployContract("Escrow", [
            seller.address,
            arbiter.address,
            fee
        ], {
            value: ethers.parseUnits("100", "wei"),
            signer: buyer
        }));

        return { Escrow, buyer, seller, arbiter, fee };
    };

    it("auth-in-agree", async function() {
        const { Escrow, buyer, seller, arbiter } = await loadFixture(deployContract);
      
        expect(await Escrow.connect(arbiter).arbitrate(seller.address)).to.not.be.reverted;
    });

    it("no-send-in-agree", async function() {
        const { Escrow, buyer, seller, arbiter } = await loadFixture(deployContract);

        EscrowAddress = await Escrow.getAddress()
        balanceBefore = Escrow.deposit

        await Escrow.connect(arbiter).arbitrate(seller.address)

        balanceAfter = Escrow.deposit

        expect(balanceAfter).not.to.equal(balanceBefore);
    });
}) 