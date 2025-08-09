const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

const { expect } = require("chai");


describe("Crowdfund", function () {

    async function deployContract() {

        const signers = await ethers.getSigners();

        const owner = signers[0];
        const donor = signers[1];
        
        const CrowdFund = await ethers.deployContract("Crowdfund", [
            owner.address,
            3,
            1000
        ]);

        return { CrowdFund, donor };
    };

    it("donate-not-revert reverts for an overflow", async function () {

        const { CrowdFund, donor } = await loadFixture(deployContract);
        
        

        expect(await CrowdFund.connect(donor).donate({value: amount})).to.be.reverted;
    });
      
    it("donate-not-revert reverts for an overflow", async function () {

        const { CrowdFund, donor } = await loadFixture(deployContract);
        
        // set the donation amount to a value that will cause an overflow
        const amount = BigInt("115792089237316195423570985008687907853269984665640564039457584007913129639934");

        const t = "0x" + (BigInt("115792089237316195423570985008687907853269984665640564039457584007913129639935")).toString(16)
        await network.provider.send("hardhat_setBalance", [
            donor.address,
            t 
        ]
        )
        
        await CrowdFund.connect(donor).donate({value: amount})

        const amount2 = ethers.parseUnits('3','Wei');

        expect(await CrowdFund.connect(donor).donate({value: amount})).to.be.reverted;
    });
});