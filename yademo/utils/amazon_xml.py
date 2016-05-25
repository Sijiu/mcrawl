
# -*- coding: utf-8 -*-



FeedFrame = """<?xml version="1.0" encoding="utf-8"?>
    <AmazonEnvelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="amznenvelope.xsd">
        <Header>
            <DocumentVersion>1.01</DocumentVersion>
            <MerchantIdentifier>%s</MerchantIdentifier>
        </Header>
        <MessageType>%s</MessageType>
        %s
    </AmazonEnvelope>"""
BasicMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <Product>
            <SKU>%(SKU)s</SKU>
            %(StandardProductID)s
            <Condition>
                <ConditionType>%(ConditionName)s</ConditionType>
            </Condition>
            <DescriptionData>
                <Title>%(Title)s</Title>
                <Brand>%(Brand)s</Brand>
                <Description>
                    <![CDATA[%(Description)s]]>
                </Description>
                %(BulletPointList)s
                %(ShippingWeight)s
                %(MSRP)s
                <Manufacturer>%(Manufacturer)s</Manufacturer>
                %(MfrPartNumber)s
                %(SearchTermsList)s
                %(ItemType)s
                %(TargetAudience)s
            </DescriptionData>
            <ProductData>
                %(ProductData)s
            </ProductData>
        </Product>
    </Message>"""
SoldBasicMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <Product>
            <SKU>%(SKU)s</SKU>
            <StandardProductID>
                <Type>ASIN</Type>
                <Value>%(Asin)s</Value>
            </StandardProductID>
            <Condition>
                <ConditionType>%(ConditionName)s</ConditionType>
            </Condition>
            <DescriptionData>
                <Title>%(Title)s</Title>
            </DescriptionData>
        </Product>
    </Message>"""
StockMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <Inventory>
            <SKU>%(SKU)s</SKU>
            <Quantity>%(Stock)s</Quantity>
            %(DispatchTimeMax)s
        </Inventory>
    </Message>"""
PriceMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <Price>
            <SKU>%(SKU)s</SKU>
            <StandardPrice currency="%(Currency)s">%(Price)s</StandardPrice>
            %(Sale)s
        </Price>
    </Message>"""
ImageMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <ProductImage>
            <SKU>%(SKU)s</SKU>
            <ImageType>Main</ImageType>
            <ImageLocation>%(Image)s</ImageLocation>
        </ProductImage>
    </Message>
    %(OtherImages)s
"""
RelationMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <Relationship>
            <ParentSKU>%(ParentSKU)s</ParentSKU>
            %(RelationList)s
        </Relationship>
    </Message>
"""
OfflineMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Delete</OperationType>
        <Product>
            <SKU>%(SKU)s</SKU>
        </Product>
    </Message>"""

NewPriceMessage = """<Message>
        <MessageID>%(MessageID)s</MessageID>
        <OperationType>Update</OperationType>
        <Price>
            <SKU>%(SKU)s</SKU>
            %(Price)s
            %(Sale)s
        </Price>
    </Message>"""

UpdateBase = """<Message>
    <MessageID>%(MessageID)s</MessageID>
    <OperationType>PartialUpdate</OperationType>
    <Product>
        <SKU>%(SKU)s</SKU>
        <DescriptionData>
            <Title>%(Title)s</Title>
            %(Description)s
            %(BulletPointList)s
            %(SearchTermsList)s
            %(ItemType)s
        </DescriptionData>
    </Product>
</Message>"""

CEProductData = """<CE>
        <ProductType>
            <ConsumerElectronics>%s</ConsumerElectronics>
        </ProductType>
        %s
    </CE>
"""
ToysData = """<Toys>%s
        <ProductType>%s</ProductType>
        <AgeRecommendation>
            <MinimumManufacturerAgeRecommended unitOfMeasure=\"%s\">%s</MinimumManufacturerAgeRecommended>
        </AgeRecommendation>
        %s
    </Toys>
"""
ClothingProductData = """<Clothing>%s</Clothing>"""

HomeData = """<Home><ProductType><Home>%s</Home></ProductType>%s</Home>"""

KitchenDate = """<Home><ProductType><Kitchen>%s</Kitchen ></ProductType>%s</Home>"""

SportsData = """<Sports><ProductType>%s</ProductType><VariationData>%s</VariationData></Sports>"""

ComputersData = """<Computers>
    <ProductType>
        <%s>
            %s
        </%s>
    </ProductType>
    %s
    %s
</Computers>"""

__all__ = ['FeedFrame', 'BasicMessage', 'ImageMessage', 'RelationMessage', "OfflineMessage",
           'PriceMessage', 'StockMessage', "CEProductData", "ClothingProductData", "ComputersData"]