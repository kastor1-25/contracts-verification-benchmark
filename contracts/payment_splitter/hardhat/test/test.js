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



/** */

        const Returns7 = await(ethers.deployContract("ReturnsN", [7], {
            value: ethers.parseUnits("7", "wei")
        }));
        const Returns5 = await(ethers.deployContract("ReturnsN", [5], {
            value: ethers.parseUnits("5", "wei")
        }));

        const payees_swap_test = [
            Returns7.getAddress(),
            Returns5.getAddress()
        ];
        const PaymentSplitter_swap_test = await(ethers.deployContract("PaymentSplitter", [
            payees_swap_test,
            [1,1]
        ], {
            value: ethers.parseUnits("8", "wei")
        }));

        return { PaymentSplitter, RevertOnReceive , PaymentSplitter2, payees,   PaymentSplitter_swap_test, payees_swap_test };
    };



    // These revert, so I don't think they are useful
    /*
    it("release when funds are insufficient for a fair split should fail", async function() {
        const { PaymentSplitter2, payees } = await loadFixture(deployContract);
        const balanceBefore = await PaymentSplitter2.balanceOf(PaymentSplitter2.getAddress());
       
        await PaymentSplitter2.release(payees[0]);
        expect(await PaymentSplitter2.balanceOf(PaymentSplitter2.getAddress())).not.to.equal(balanceBefore);
    })
    */


    it("release but it reverts", async function () {
        const { PaymentSplitter, RevertOnReceive } = await loadFixture(deployContract);
        
        const balanceBefore = await PaymentSplitter.balanceOf(PaymentSplitter.getAddress());

        await expect(
            PaymentSplitter.release(RevertOnReceive.getAddress())
            ).to.be.reverted;

        const balanceAfter = await PaymentSplitter.balanceOf(PaymentSplitter.getAddress());

        expect(balanceAfter).to.equal(balanceBefore); // not important, property still holds
    });


    it("swap", async function () {
        var balanceAfter1, balanceAfter2;

        // Run 1: first payee[0] calls release, then payee[1]

        {
            const { PaymentSplitter, RevertOnReceive , PaymentSplitter2, payees,   PaymentSplitter_swap_test, payees_swap_test } = await loadFixture(deployContract);

            expect (payees_swap_test[0]).not.to.equal(payees_swap_test[1]);
            
            await PaymentSplitter_swap_test.release(payees_swap_test[0]);
            await PaymentSplitter_swap_test.release(payees_swap_test[1]);

            balanceAfter1 = await PaymentSplitter_swap_test.balanceOf(PaymentSplitter_swap_test.getAddress());
        }

        // Run 2: first payee[1] calls release, then payee[0]

        {
            const { PaymentSplitter, RevertOnReceive , PaymentSplitter2, payees,   PaymentSplitter_swap_test, payees_swap_test } = await loadFixture(deployContract);
            
            expect (payees_swap_test[0]).not.to.equal(payees_swap_test[1]);

            await PaymentSplitter_swap_test.release(payees_swap_test[1]);
            await PaymentSplitter_swap_test.release(payees_swap_test[0]);

            balanceAfter2 = await PaymentSplitter_swap_test.balanceOf(PaymentSplitter_swap_test.getAddress());
        }


        // Confront the two runs
        expect(balanceAfter1).not.to.equal(balanceAfter2);
    });
});