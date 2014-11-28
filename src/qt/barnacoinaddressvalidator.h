// Copyright (c) 2011-2014 The Bitcoin developers
// Distributed under the MIT/X11 software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef BARNACOINADDRESSVALIDATOR_H
#define BARNACOINADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class BarnacoinAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit BarnacoinAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

/** Barnacoin address widget validator, checks for a valid barnacoin address.
 */
class BarnacoinAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit BarnacoinAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

#endif // BARNACOINADDRESSVALIDATOR_H
